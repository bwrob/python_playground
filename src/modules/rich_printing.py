"""Example of Rich Printing."""

from icecream import ic, install
from rich import inspect
from rich import print as rich_print

install()


if __name__ == "__main__":
    rich_print("Hello, World!")
    rich_print("[italic red]Hello[/italic red] World!")

    rich_print(locals())
    ic(locals())

    ic(__builtins__)
    rich_print(__builtins__)
    inspect(__builtins__)
