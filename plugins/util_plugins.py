import importlib
import os

class PluginLoader:

    def __init__(self, plugin_type: str):
        """
        arg: plugin_type: str 
            plugin_type which should be child directory of plugins
        """
        self.plugin_type = plugin_type
        self.plugins = self._load_plugins()

    def _discover_plugins(self) -> list:
        """
        Finds plugins by looking in directory plugins/plugin_type
        Return a list of plugin locations
        """
        path = f"./plugins/{self.plugin_type}/"
        dirs = os.listdir(path)
        plugins = [{"name": file, "plugin": f"plugins.{self.plugin_type}.{file}.{file}"} for file in dirs if os.path.isdir(f"{path}{file}") and os.path.isfile(f"{path}{file}/{file}.py")]
        return plugins
    
    def _load_plugins(self) -> dict:
        """
        Loads and initialises the plugins from the plugin_type
        Returns a dictionary of plugins
        """
        plugins = self._discover_plugins()
        return {plugin['name']: importlib.import_module(plugin['plugin']).Plugin() for plugin in plugins}

