class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
            self.tag = tag            # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
            self.value = value        # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
            self.children = children  # A list of HTMLNode objects representing the children of this node
            self.props = props        # A dictionary of key-value pairs representing the attributes of the HTML tag

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            self.props = {}
        return ''.join(f' {key}="{value}"' for key, value in self.props.items())

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f'HTMLNode(TAG="{self.tag}", VALUE="{self.value}", CHILDREN={self.children}, PROPS={self.props_to_html()})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value
        self.props = props if props is not None else {}
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value is None or len(self.value) == 0:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None or len(self.tag) == 0:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.children = children
        self.props = props if props is not None else {}
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or len(self.tag) == 0:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("All parent nodes must have children")
        return f'<{self.tag}{self.props_to_html()}>{"".join(child.to_html() for child in self.children)}</{self.tag}>'
