import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_1(self):
        node = TextNode("this is not equal", TextType.BOLD, "boot.dev")
        node2 = TextNode("This is shit", TextType.LINK)
        self.assertNotEqual(node, node2)
    
    def test_2(self):
        node = TextNode("This is shit", TextType.BOLD, "boot.dev")
        node2 = TextNode("This is shit", TextType.LINK)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()