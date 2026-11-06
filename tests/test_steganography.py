"""Run with: python -m unittest discover -s tests"""
import tempfile
import unittest
from pathlib import Path

from PIL import Image
from hideRead import solve


class SteganographyTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        self.original = self.root / "original.png"
        Image.new("RGB", (80, 80), (130, 201, 255)).save(self.original)
        self.encoded = self.root / "hidden.png"

    def test_unicode_round_trip_and_unmodified_source(self):
        message = "Hello, София! 🐈\n0123456789"
        solve("H", str(self.original), None, message, str(self.encoded), "n")
        self.assertEqual(
            solve("R", str(self.original), str(self.encoded), "", "", "n"), message
        )
        with Image.open(self.original) as source:
            self.assertEqual(source.getpixel((0, 0)), (130, 201, 255))

    def test_red_channel_boundary_values(self):
        Image.new("RGB", (100, 100), (255, 0, 1)).save(self.original)
        solve("H", str(self.original), None, "A", str(self.encoded), "n")
        self.assertEqual(solve("R", str(self.original), str(self.encoded), "", "", "n"), "A")

    def test_capacity_guard(self):
        Image.new("RGB", (2, 2), (0, 0, 0)).save(self.original)
        with self.assertRaisesRegex(ValueError, "too long"):
            solve("H", str(self.original), None, "A", str(self.encoded), "n")
        self.assertFalse(self.encoded.exists())

    def test_mismatch_and_missing_header(self):
        with self.assertRaisesRegex(ValueError, "header"):
            solve("R", str(self.original), str(self.original), "", "", "n")
        Image.new("RGB", (20, 20), (0, 0, 0)).save(self.encoded)
        with self.assertRaisesRegex(ValueError, "dimensions"):
            solve("R", str(self.original), str(self.encoded), "", "", "n")


if __name__ == "__main__":
    unittest.main()
