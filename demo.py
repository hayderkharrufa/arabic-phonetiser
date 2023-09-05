import arabic_phonetiser
from arabic_buckwalter_transliteration.transliteration import buckwalter_to_arabic, arabic_to_buckwalter

arabic_text = "أگُلّـچْ يَبـنْتي وأَسَمْعـچْ يَچَنْتي"
buck_text = arabic_to_buckwalter(arabic_text)
phon_text = arabic_phonetiser.arabic_to_phonemes(buck_text)
print(phon_text)
