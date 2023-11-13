# file and folder structure used from https://github.com/kevyt/james

import yaml
import pandas as pd

import plugins.create
import plugins.save
import plugins.df_manipulation


def read_config(filepath: str ="./data/config.yaml") -> dict:
    """
    Reads configuration file from a given path
    """
    with open(filepath, 'r') as file:
        config = yaml.safe_load(file)
    return config

def _create(create_config, dfs, pluginrepo: dict={}) -> pd.DataFrame:
    df = pd.DataFrame()
    for variable, config in create_config['steps'].items():
        for plugin, params in config.items():
            payload = {
                'kolomnaam': variable,
                'df': df,
                'params': params,
                "veelheid": create_config['amount_values']

            }
            df = pluginrepo[plugin].process(payload)
    
    return df

def _save(save_config, dfs, pluginrepo: dict={}) -> pd.DataFrame:
    for variable, config in save_config['steps'].items():
        for plugin, params in config.items():
            payload = {
                'df': dfs[variable],
                'params': params
            }
            df = pluginrepo[plugin].process(payload)
    return df

def _df_manipulation(save_config, dfs, pluginrepo: dict={}) -> pd.DataFrame:
    for variable, config in save_config['steps'].items():
        for plugin, params in config.items():
            payload = {
                'params': [dfs[table_name] for table_name in params]
            }
            df = pluginrepo[plugin].process(payload)
    return df

transformers = {
    "create_columns": {
        "function": _create,
        "pluginrepo": plugins.create.Plugins().plugins
    },
    "save_dataframe": {
        "function": _save,
        "pluginrepo": plugins.save.Plugins().plugins
    },
    "manipulate_dataframe": {
        "function": _df_manipulation,
        "pluginrepo": plugins.df_manipulation.Plugins().plugins
    }
}

def my_pipeline(config_filepath="./data/config.yaml", transformers=transformers):
    config = read_config(config_filepath) 
    dfs = {} # initialise an empty dictionary
    for step, step_config in config.items():
        # print(step, step_config['step_type'])  
        step_type = step_config['step_type']
        func = transformers[step_type]["function"]
        pluginrepo = transformers[step_type]["pluginrepo"]
        # print(step_config, dfs)
        
        dfs[step] = func(step_config, dfs, pluginrepo)
    print(dfs)