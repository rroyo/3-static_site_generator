import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown):
    cleaned_blocks = []
    blocks = markdown.split("\n\n")

    for block in blocks:
        if block == "":
            continue

        cleaned_blocks.append(block.strip())

    return cleaned_blocks


def is_ordered_list(block):
    lines = block.split("\n")
    for index, line in enumerate(lines):
        if not (re.match(rf"^{index+1}\.\s+", line.strip())):
            return False
    return True


def block_to_block_type(block):
    re_heading = r"^(#{1,6})\s+.*"
    re_code = r"^```[\s\S]*```$"
    re_quote = re.compile(r"^>.*", re.MULTILINE)
    re_unordered_list = re.compile(r"^(\*|-)\s+.*", re.MULTILINE)

    if re.match(re_heading, block):
        return block_type_heading
    elif re.match(re_code, block):
        return block_type_code
    elif re.match(re_quote, block):
        return block_type_quote
    elif re.match(re_unordered_list, block):
        return block_type_unordered_list
    elif is_ordered_list(block):
        return block_type_ordered_list

    return block_type_paragraph
