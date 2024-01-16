from types import ModuleType


class PluginModule(ModuleType):
    def load_plugin(self): ...
