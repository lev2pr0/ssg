from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    valid_delimiters = ["**", "_", "`"]
    if delimiter not in valid_delimiters:
        raise ValueError(f"Invalid Markdown delimiter: '{delimiter}'")

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
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

def split_nodes_image(old_nodes):

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        img_ext = extract_markdown_images(original_text)
        if len(img_ext) == 0:
            new_nodes.append(node)
            continue
        for image in img_ext:

            image_alt = image[0]
            image_link = image[1]

            sections = original_text.split(f"![{image_alt}]({image_link})", 1)

            before_img = sections[0]
            after_img = sections[1]

            if len(before_img) != 0:
                new_nodes.append(TextNode(before_img, TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                original_text = after_img
            else:
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                original_text = after_img
        if len(original_text) != 0:
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):

    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        original_text = node.text
        link_ext = extract_markdown_links(original_text)
        if len(link_ext) == 0:
            new_nodes.append(node)
            continue
        for link in link_ext:

            link_text = link[0]
            link_url = link[1]

            sections = original_text.split(f"[{link_text}]({link_url})", 1)

            before_link = sections[0]
            after_link = sections[1]

            if len(before_link) != 0:
                new_nodes.append(TextNode(before_link, TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                original_text = after_link
            else:
                new_nodes.append(TextNode(link_text, TextType.IMAGE, link_url))
                original_text = after_link
        if len(original_text) != 0:
            new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
