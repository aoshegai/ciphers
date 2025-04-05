import unittest
from caesar_cipher import caesar_cipher

class TestCaesarCipher(unittest.TestCase):

    def test_encryption(self):
        self.assertEqual(caesar_cipher("Hello World!", 3), "Khoor Zruog!")
        self.assertEqual(caesar_cipher("abc", 1), "bcd")
        self.assertEqual(caesar_cipher("xyz", 3), "abc")
        
    def test_decryption(self):
        self.assertEqual(caesar_cipher("Khoor Zruog!", -3), "Hello World!")
        self.assertEqual(caesar_cipher("bcd", -1), "abc")
        self.assertEqual(caesar_cipher("abc", -3), "xyz")

    def test_non_alpha_characters(self):
        self.assertEqual(caesar_cipher("1234! @#$", 4), "1234! @#$")
        self.assertEqual(caesar_cipher("A B C", 2), "C D E")

if __name__ == "__main__":
    unittest.main()