# The HTMLNode class will represent a "node" in an HTML document tree (like a <p> tag and its contents,
# or an <a> tag and its contents) and is purpose-built to render itself as HTML.


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html not implemented")

    def props_to_html(self):
        props_string = ""

        if self.props:
            for key, value in self.props.items():
                props_string = f'{props_string} {key}="{value}"'
        return props_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
