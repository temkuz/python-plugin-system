from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import sys

from poc_plugin.variables.plugin import PLUGINS_DIR

from poc_plugin.types.plugins import PluginModule
from .validator import PluginValidator


class PluginSystem:
    @classmethod
    def load_plugins(cls):
        """
        Loads plugins from the PLUGINS_DIR folder
        """
        for current_dir, folders, files in PLUGINS_DIR.walk():
            if not PluginValidator.is_plugin(files):
                continue
            module = cls.get_module(current_dir)
            cls.load_plugin(module)

    @staticmethod
    def get_module(current_dir: Path) -> PluginModule:
        """
        Generates a plugin
        """
        module_name = current_dir.name
        spec = spec_from_file_location(module_name, current_dir / '__init__.py')
        module = module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module

    @staticmethod
    def load_plugin(module: PluginModule):
        """
        Load plugin
        """
        if load_plugin := PluginValidator.has_load_plugin_function(module):
            load_plugin()
