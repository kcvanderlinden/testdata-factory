# file and folder structure used from https://github.com/kevyt/james

import yaml
import pandas as pd

import plugins.create
import plugins.save


def read_config(filepath: str ="./data/config.yaml") -> dict:
    """
    Reads configuration file from a given path
    """
    with open(filepath, 'r') as file:
        config = yaml.safe_load(file)
    return config

def parse_cleaning_steps(df: pd.DataFrame, cleaning_steps: dict) -> dict:
    for variable, config in cleaning_steps.items():
        if "based_on" in config:
            base_cleaning_steps = cleaning_steps[config['based_on']]
            for k,v in base_cleaning_steps.items():
                if k not in cleaning_steps[variable]:
                    cleaning_steps[variable][k] = v
            cleaning_steps[variable].pop('based_on')
        if "type" in config:
            cleaning_steps[variable].pop('type')

    cleaning_steps = {key: value for key, value in cleaning_steps.items() if key in df.columns}
    return cleaning_steps

def _read(read_config, df=None, pluginrepo: dict={}) -> pd.DataFrame:
    config=read_config
    dfs_out = {}
    for name, fileconf in config['files'].items():
        df, meta = pluginrepo[fileconf['filetype']].process(f"./data/{fileconf['filename']}")
        dfs_out[name] = {
            'df': df,
            'meta': meta
        }
    return dfs_out

def _clean(cleaning_config, dfs={}, pluginrepo: dict={}) -> pd.DataFrame:

    for name, config in dfs.items():
        if 'apply_to' in cleaning_config and name not in cleaning_config['apply_to']:
            continue
        print(f"Cleaning on {name}")
        df = config['df']
        cleaning_steps = parse_cleaning_steps(df, cleaning_config['steps'])
        for variable, config in cleaning_steps.items():
            for plugin, params in config.items():
                payload = {
                    'variable': variable,
                    'df': df,
                    'params': params
                }
                df = pluginrepo[plugin].process(payload)
        dfs[name]['df'] = df
    return dfs

def _transform(transform_config, dfs={}, pluginrepo: dict={}) ->pd.DataFrame:
    for name, config in dfs.items():
        if 'apply_to' in transform_config and name not in transform_config['apply_to']:
            continue
        print(f"Transforming {name}")
        df = config['df']
        for stepname, config in transform_config['steps'].items():
            print(f"Transform {stepname}")
            for plugin, plugin_config in config.items():
                payload = {
                    'df': df,
                    'params': plugin_config
                }
                df = pluginrepo[plugin].process(payload)
        dfs[name]['df'] = df
    return dfs

def _aggregate(aggregate_config, dfs={}) ->pd.DataFrame:
    return df

transformers = {
    "readfile": {
        "function": _read,
        "pluginrepo": plugins.read.Plugins().plugins
    },
    "cleaning": {
        "function": _clean,
        "pluginrepo": plugins.clean.CleaningPlugins().plugins
    },
    "transformation": {
        "function": _transform,
        "pluginrepo": plugins.transform.Plugins().plugins
    }
}

def my_pipeline(config_filepath="./data/config.yaml", transformers=transformers):
    config = read_config(config_filepath) 
    dfs = {} #initialise an empty dataframe
    for step, step_config in config.items():
        print(step, step_config['step_type'])  
        step_type = step_config['step_type']
        func = transformers[step_type]["function"]
        pluginrepo = transformers[step_type]["pluginrepo"]
        dfs = func(step_config, dfs, pluginrepo)
    print(dfs)