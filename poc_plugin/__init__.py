from poc_plugin.plugin import PluginSystem
from poc_plugin.variables import CLI_UTILS


def main():
    PluginSystem.load_plugins()
    namespace = CLI_UTILS.parser.parse_args()
    if 'func' in namespace:
        namespace.func(namespace)


if __name__ == '__main__':
    main()
