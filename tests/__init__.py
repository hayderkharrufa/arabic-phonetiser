import unittest
from arabic_phonetiser import arabic_to_phonemes

class TestPhonetiser(unittest.TestCase):

    def test_arabic_to_phonemes(self):
        arabic_text = "أگُلّـچْ يَبـنْتي وأَسَمْعـچْ يَچَنْتي"
        expected_output = "< a G u0 ll ı C + y a b ı n t ii0 + uu0 < a s a m E ı C + y a C a n t ii0"
        
        self.assertEqual(arabic_to_phonemes(arabic_text), expected_output)

if __name__ == "__main__":
    unittest.main()