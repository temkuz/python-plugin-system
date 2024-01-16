from poc_plugin.plugin import PluginSystem
from poc_plugin.variables.cli import CLI_PARSER


def main():
    PluginSystem.load_plugins()
    namespace = CLI_PARSER.parse_args()
    if 'func' in namespace:
        namespace.func(namespace)


if __name__ == '__main__':
    main()
