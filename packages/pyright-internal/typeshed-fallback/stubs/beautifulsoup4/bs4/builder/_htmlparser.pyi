from _typeshed import Incomplete
from html.parser import HTMLParser
from typing import Any

from bs4.builder import HTMLTreeBuilder

class HTMLParseError(Exception): ...

class BeautifulSoupHTMLParser(HTMLParser):
    IGNORE: str
    REPLACE: str
    on_duplicate_attribute: Any
    already_closed_empty_element: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def error(self, msg: str) -> None: ...
    def handle_startendtag(self, name, attrs) -> None: ...
    def handle_starttag(self, name, attrs, handle_empty_element: bool = ...) -> None: ...
    def handle_endtag(self, name, check_already_closed: bool = ...) -> None: ...
    def handle_data(self, data) -> None: ...
    def handle_charref(self, name) -> None: ...
    def handle_entityref(self, name) -> None: ...
    def handle_comment(self, data) -> None: ...
    def handle_decl(self, data) -> None: ...
    def unknown_decl(self, data) -> None: ...
    def handle_pi(self, data) -> None: ...

class HTMLParserTreeBuilder(HTMLTreeBuilder):
    is_xml: bool
    picklable: bool
    NAME: Any
    features: Any
    TRACKS_LINE_NUMBERS: bool
    parser_args: Any
    def __init__(self, parser_args: Incomplete | None = ..., parser_kwargs: Incomplete | None = ..., **kwargs) -> None: ...
    def prepare_markup(
        self,
        markup,
        user_specified_encoding: Incomplete | None = ...,
        document_declared_encoding: Incomplete | None = ...,
        exclude_encodings: Incomplete | None = ...,
    ) -> None: ...
    def feed(self, markup) -> None: ...
