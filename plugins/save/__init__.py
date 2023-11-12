from plugins.util_plugins import PluginLoader

class Plugins:

    def __init__(self):
        self.plugins = PluginLoader("save").plugins