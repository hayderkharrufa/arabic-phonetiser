import text
from arabic_buckwalter_transliteration.transliteration import buckwalter_to_arabic, arabic_to_buckwalter

arabic_text = "أگُلّـچْ يَبـنْتي وأَسَمْعـچْ يَچَنْتي"
buck_text = arabic_to_buckwalter(arabic_text)
phon_text = text.arabic_to_phonemes(buck_text)
print(buck_text)
print(text.simplify_phonemes(phon_text))