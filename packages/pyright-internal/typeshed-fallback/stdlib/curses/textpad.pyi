import sys
from collections.abc import Callable

if sys.platform != "win32":
    from _curses import _CursesWindow
    def rectangle(win: _CursesWindow, uly: int, ulx: int, lry: int, lrx: int) -> None: ...

    class Textbox:
        stripspaces: bool
        def __init__(self, win: _CursesWindow, insert_mode: bool = False) -> None: ...
        def edit(self, validate: Callable[[int], int] | None = None) -> str: ...
        def do_command(self, ch: str | int) -> None: ...
        def gather(self) -> str: ...
