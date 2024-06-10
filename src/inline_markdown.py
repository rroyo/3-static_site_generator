import re
from textnode import TextNode, TextType, TextTypeDelimiter


# Returns a list of TextNodes split by TextType and text_type types
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT.value))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_delimiter_meu(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT.value:
            new_nodes.append(old_node)
            continue

        first_delimiter_index = old_node.text.find(delimiter)
        second_delimiter_index = old_node.text[first_delimiter_index + 1 :].find(
            delimiter
        )

        if second_delimiter_index == -1:
            raise Exception("Invalid Markdown syntax")

        new_nodes.append(
            TextNode(old_node.text[:first_delimiter_index], TextType.TEXT.value)
        )

        new_nodes.append(
            TextNode(
                old_node.text[
                    first_delimiter_index + 1 : first_delimiter_index
                    + second_delimiter_index
                    + 1
                ],
                text_type,
            )
        )

        new_nodes.append(
            TextNode(
                old_node.text[first_delimiter_index + second_delimiter_index + 2 :],
                TextType.TEXT.value,
            )
        )

    return new_nodes


# Returns a list of tuples [(Alt Text, Image URL), ...]
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


# Returns a list of tuples [(Link Text, Link URL), ...]
def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        image_tuples = extract_markdown_images(old_node.text)

        if len(image_tuples) == 0:
            new_nodes.append(old_node)
            continue

        text_to_split = old_node.text

        for image_tuple in image_tuples:
            split_nodes = text_to_split.split(
                f"![{image_tuple[0]}]({image_tuple[1]})", 1
            )

            text_to_split = split_nodes[1]

            if split_nodes[0] == "":
                new_nodes.append(
                    TextNode(image_tuple[0], TextType.IMAGE.value, image_tuple[1])
                )
            else:
                new_nodes.extend(
                    [
                        TextNode(split_nodes[0], TextType.TEXT.value),
                        TextNode(image_tuple[0], TextType.IMAGE.value, image_tuple[1]),
                    ]
                )
        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, TextType.TEXT.value))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        link_tuples = extract_markdown_links(old_node.text)

        if len(link_tuples) == 0:
            new_nodes.append(old_node)
            continue

        text_to_split = old_node.text

        for link_tuple in link_tuples:
            split_nodes = text_to_split.split(f"[{link_tuple[0]}]({link_tuple[1]})", 1)

            text_to_split = split_nodes[1]

            if split_nodes[0] == "":
                new_nodes.append(
                    TextNode(link_tuple[0], TextType.LINK.value, link_tuple[1])
                )
            else:
                new_nodes.extend(
                    [
                        TextNode(split_nodes[0], TextType.TEXT.value),
                        TextNode(link_tuple[0], TextType.LINK.value, link_tuple[1]),
                    ]
                )
        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, TextType.TEXT.value))

    return new_nodes


# Takes a TextNode, returns a list of TextNodes split by type
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT.value)]
    nodes = split_nodes_delimiter(
        nodes, TextTypeDelimiter.CODE.value, TextType.CODE.value
    )
    nodes = split_nodes_delimiter(
        nodes, TextTypeDelimiter.BOLD.value, TextType.BOLD.value
    )
    nodes = split_nodes_delimiter(
        nodes, TextTypeDelimiter.ITALIC.value, TextType.ITALIC.value
    )
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
