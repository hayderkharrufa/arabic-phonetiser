import arabic_phonetiser

arabic_text = "أگُلّـچْ يَبـنْتي وأَسَمْعـچْ يَچَنْتي"
phon_text = arabic_phonetiser.arabic_to_phonemes(arabic_text)
print(phon_text)
