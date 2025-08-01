from textnode import *

def main():
    result = TextNode(
        "This is some anchor text",
        TextType.LINK,
        "https://www.boot.dev"
    )

    print(result)


main()
