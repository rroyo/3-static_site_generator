from textnode import TextNode

def main():
    node1 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    node3 = TextNode("This is a text node", "bold")
    print(node1.__eg__(node2))
    print(node1.__eg__(node2))
    print(node3)

main()