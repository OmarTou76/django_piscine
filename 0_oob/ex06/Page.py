from elem import Elem, Text
from elements import (
    Html,
    Head,
    Body,
    Title,
    Meta,
    Img,
    Table,
    Th,
    Tr,
    Td,
    Ul,
    Ol,
    Li,
    H1,
    H2,
    P,
    Div,
    Span,
    Hr,
    Br,
)


class Page:
    def __init__(self, elem):
        if not isinstance(elem, Elem):
            raise TypeError("Page must be initialized with an Elem instance")
        self.root = elem

    def __str__(self):
        html = str(self.root)
        if isinstance(self.root, Html):
            return "<!DOCTYPE html>\n" + html
        return html

    def write_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as fd:
            fd.write(str(self))

    def is_valid(self):
        allowed_types = (
            Html,
            Head,
            Body,
            Title,
            Meta,
            Img,
            Table,
            Th,
            Tr,
            Td,
            Ul,
            Ol,
            Li,
            H1,
            H2,
            P,
            Div,
            Span,
            Hr,
            Br,
        )

        body_div_allowed = (H1, H2, Div, Table, Ul, Ol, Span, Text)

        def only_one_text(node):
            return len(node.content) == 1 and type(node.content[0]) is Text

        def validate_node(node):
            if type(node) is Text:
                return True

            if not isinstance(node, allowed_types):
                return False

            children = node.content

            if isinstance(node, Html):
                if len(children) != 2:
                    return False
                if not isinstance(children[0], Head):
                    return False
                if not isinstance(children[1], Body):
                    return False

            elif isinstance(node, Head):
                if len(children) != 1 or not isinstance(children[0], Title):
                    return False

            elif isinstance(node, (Body, Div)):
                if not all(isinstance(child, body_div_allowed) for child in children):
                    return False

            elif isinstance(node, (Title, H1, H2, Li, Th, Td)):
                if not only_one_text(node):
                    return False

            elif isinstance(node, P):
                if not all(type(child) is Text for child in children):
                    return False

            elif isinstance(node, Span):
                if not all(isinstance(child, (Text, P)) for child in children):
                    return False

            elif isinstance(node, (Ul, Ol)):
                if len(children) == 0:
                    return False
                if not all(isinstance(child, Li) for child in children):
                    return False

            elif isinstance(node, Tr):
                if len(children) == 0:
                    return False
                if all(isinstance(child, Th) for child in children):
                    pass
                elif all(isinstance(child, Td) for child in children):
                    pass
                else:
                    return False

            elif isinstance(node, Table):
                if not all(isinstance(child, Tr) for child in children):
                    return False

            for child in children:
                if type(child) is Text:
                    continue
                if not validate_node(child):
                    return False
            return True

        return validate_node(self.root)


if __name__ == "__main__":
    valid_page = Page(
        Html([
            Head([Title(Text("Valid HTML"))]),
            Body([
                H1(Text("H1 Test")),
                H2(Text("H2 Test")),
                Div([
                    Span([
                        Text("Text in Span Test"),
                    ]),
                    H2(Text("Text in H2")),
                    Ol([
                        Li(Text("Lorem ipsum dolor sit amet")),
                        Li(Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit")),
                        Li(Text("Lorm ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua")),
                    ]),
                    H2(Text("Next Priorities")),
                    Ul([
                        Li(Text("Refactor demo pages for readability")),
                        Li(Text("Expand test cases for edge conditions")),
                        Li(Text("Prepare final review before submission")),
                    ]),
                    H2(Text("Time Allocation")),
                    Table([
                        Tr([Th(Text("Category")), Th(Text("Hours"))]),
                        Tr([Td(Text("Coding")), Td(Text("10"))]),
                        Tr([Td(Text("Testing")), Td(Text("4"))]),
                        Tr([Td(Text("Documentation")), Td(Text("2"))]),
                    ]),
                    Span([P([Text("Lorem ipsum dolor sit amet"), Text("Keep Testing.")])]),
                ]),
            ]),
        ])
    )

    invalid_html_structure = Page(
        Html([
            Body([H1(Text("Wrong order"))]),
            Head([Title(Text("bad"))]),
        ])
    )

    invalid_head_structure = Page(
        Html([
            Head([Title(Text("ok")), Meta({"charset": "utf-8"})]),
            Body([H1(Text("hello"))]),
        ])
    )

    invalid_tr_mix = Page(
        Html([
            Head([Title(Text("mix"))]),
            Body([
                Table([
                    Tr([
                        Th(Text("h")),
                        Td(Text("d")),
                    ])
                ])
            ]),
        ])
    )

    invalid_span = Page(
        Html([
            Head([Title(Text("span"))]),
            Body([
                Span([
                    Div([H1(Text("not allowed inside span"))])
                ])
            ]),
        ])
    )

    not_html_root = Page(Div([P([Text("No doctype expected")])]))

    assert valid_page.is_valid() is True
    assert invalid_html_structure.is_valid() is False
    assert invalid_head_structure.is_valid() is False
    assert invalid_tr_mix.is_valid() is False
    assert invalid_span.is_valid() is False

    assert str(valid_page).startswith("<!DOCTYPE html>\n")
    assert str(not_html_root).startswith("<div")
    assert "<!DOCTYPE html>" not in str(not_html_root)

    output_file = "page_output_test.html"
    valid_page.write_to_file(output_file)
    with open(output_file, "r", encoding="utf-8") as fd:
        data = fd.read()
    assert data.startswith("<!DOCTYPE html>\n")

    print("All Page tests passed.")
