"""Example of Rich Printing."""

from icecream import ic, install
from rich import inspect
from rich import print as rich_print

install()


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a} {self.b}"

    def do_something(self):
        return self.a + self.b


if __name__ == "__main__":
    rich_print("Hello, World!")
    rich_print("[italic red]Hello[/italic red] World!")

    rich_print(locals())
    ic(locals())

    ic(__builtins__)
    rich_print(__builtins__)
    inspect(__builtins__)

    example_obj = MyClass(1, 2)
    inspect(MyClass, all=True)
    inspect(example_obj, all=True)

    inspect(inspect)
