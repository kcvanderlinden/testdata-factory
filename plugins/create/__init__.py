from plugins.util_plugins import PluginLoader

class CleaningPlugins:

    def __init__(self):
        self.plugins = PluginLoader("create").plugins