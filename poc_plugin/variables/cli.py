from argparse import ArgumentParser

from poc_plugin.types.cli import CLIUtils

CLI_PARSER = ArgumentParser()
CLI_SUBPARSER = CLI_PARSER.add_subparsers()

CLI_UTILS = CLIUtils(CLI_PARSER, CLI_SUBPARSER)
