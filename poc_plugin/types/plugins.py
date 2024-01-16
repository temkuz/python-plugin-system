from types import ModuleType

from poc_plugin.types import CLIUtils


class PluginModule(ModuleType):

    def config_cli(self, cli_utils: CLIUtils): ...

    def load_plugin(self): ...
