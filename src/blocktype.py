from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):

    headings = re.findall(r'^[#]{1,6}\s.+', block)
    code_blocks = re.findall(r'(?s)([`]{3}).*?([`]{3})', block)
    quote_blocks = re.findall(r'(?m)(^>)(.*?)$', block)
    unordered_lists = re.findall(r'(?m)(^-)(.*?)$', block)
    ordered_lists = re.findall(r'(?m)(^\d+.)(\s.*?)$', block)

    if headings:
        return BlockType.HEADING
    elif code_blocks:
        return BlockType.CODE
    elif quote_blocks:
        return BlockType.QUOTE
    elif unordered_lists:
        return BlockType.UNORDERED_LIST
    elif ordered_lists:
        number_split = block[0][0].split('.')
        if int(number_split[0]) == 1:
            for i in range(1, len(number_split)):
                if number_split[i] == '':
                    raise ValueError(f"{number_split[i]} in Ordered list must be a number")
                if number_split[i] < number_split[i-1]:
                    raise ValueError("Ordered lists must be sequential")
            return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
