import unittest
from enum import Enum


class Color(Enum):
    RED = None
    GREEN = "string"
    BLUE = 3


def color_to_hex(color):
    if color == Color.RED:
        return "#FF0000"
    if color == Color.GREEN:
        return "#00FF00"
    if color == Color.BLUE:
        return "#0000FF"
    raise Exception("Unknown color")


class TestColorToHex(unittest.TestCase):
    def test_red(self):
        self.assertEqual(color_to_hex(Color.RED), "#FF0000")

    def test_green(self):
        self.assertEqual(color_to_hex(Color.GREEN), "#00FF00")

    def test_blue(self):
        self.assertEqual(color_to_hex(Color.BLUE), "#0000FF")

    def test_unknown_color(self):
        with self.assertRaises(Exception):
            color_to_hex("Yellow")  # Passing an unknown color


if __name__ == "__main__":
    unittest.main()
