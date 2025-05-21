from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = TextNode("This is sample text", TextType.LINK, "https://example.com")
    node2 = HTMLNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
    print(node)
    print(node2)

if __name__ == "__main__":
    main()