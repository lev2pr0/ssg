from textnode import *

def main():
    result = TextNode(
        text="This is some anchor text",
        text_type="link",
        url="https://www.boot.dev"
    )

    print(result)


main()
