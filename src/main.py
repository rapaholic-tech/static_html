from textnode import TextNode, TextType

def main():
    node = TextNode("This is sample text", TextType.LINK, "https://example.com")

    print(node)

if __name__ == "__main__":
    main()