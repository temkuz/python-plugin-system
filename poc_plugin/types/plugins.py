from types import ModuleType


class PluginModule(ModuleType):
    """Basic plugin interface"""
    def load_plugin(self): ...
