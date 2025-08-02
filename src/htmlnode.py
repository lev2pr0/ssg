class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
            self.tag = tag if tag is not None else "" # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
            self.value = value if value is not None else "" # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
            self.children = children if children is not None else [] # A list of HTMLNode objects representing the children of this node
            self.props = props if props is not None else {} # A dictionary of key-value pairs representing the attributes of the HTML tag

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props == {}:
            return {}
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f'HTMLNode(TAG="{self.tag}", VALUE="{self.value}", CHILDREN={self.children}, PROPS={self.props_to_html()})'
