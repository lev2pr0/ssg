from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    valid_delimiters = ["**", "_", "`"]
    if delimiter not in valid_delimiters:
        raise ValueError(f"Invalid Markdown delimiter: '{delimiter}'")

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        if node.text.count(delimiter) % 2 == 0:
            text_split = node.text.split(delimiter)
            text_flag = True
            for text in text_split:
                if text_flag:
                    new_nodes.append(TextNode(text, TextType.TEXT))
                    text_flag = False
                else:
                    new_nodes.append(TextNode(text, text_type))
                    text_flag = True
        else:
            raise ValueError(f"Invalid Markdown syntax: '{delimiter}' matching closing delimiter not found,")

    return new_nodes
