from poc_plugin.types.plugins import PluginModule


class PluginValidator:
    @staticmethod
    def is_plugin(files: list[str]):
        return '__init__.py' in files

    @staticmethod
    def has_load_plugin_function(module: PluginModule):
        """
        Check if 'load_plugin' in module
        :raises
            ValueError if 'load_plugin' not in module
        """
        search_function = 'load_plugin'
        try:
            return getattr(module, search_function)
        except AttributeError:
            raise ValueError(f"{search_function!r} not found in module {module.__name__!r}")
