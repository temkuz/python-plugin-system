from argparse import ArgumentParser
from typing import NamedTuple


class CLIUtils(NamedTuple):
    parser: ArgumentParser
    subparser: '_SubParsersAction[ArgumentParser]'
