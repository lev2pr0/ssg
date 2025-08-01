from enum import Enum

class TextType(Enum):
    text = "text (plain)"
    bold = "**Bold text**"
    italic = "_Italic text_"
    code = "`Code text`"
    links = "[anchor text](url)"
    images = "![alt text](url)"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode(TEXT='{self.text}', TEXT_TYPE='{self.text_type}', URL='{self.url}')"
