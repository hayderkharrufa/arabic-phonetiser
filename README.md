# Arabic Phonetiser

## Introduction

This package is a Python library for phonetising Arabic text, with a focus on dialects like the Iraqi dialect. It is a fork of Nawar Halabi's [Arabic-Phonetiser](https://github.com/nawarhalabi/Arabic-Phonetiser), but differs in that it is simplified and includes characters commonly used in Arabic dialects.

## Features

- **Simplified Phonetisation**: The phonetisation process has been simplified for easier understanding and manipulation.

- **Support for Additional Arabic Characters**: This package extends the standard Arabic character set to include characters that are specific to various Arabic dialects, such as the Iraqi dialect. These additional characters are:
    - Buckwalter: `u'C'`, Arabic: 'چ', used in words like چاي
    - Buckwalter: `u'G'`, Arabic: 'گ', used in words like گول
    - Buckwalter: `u'P'`, Arabic: 'پ', used in words like پپسي
    - Buckwalter: `u'ı'`, Arabic: 'ـ', known as Taweel, used exclusively in dialectal Arabic as a vowel. Its pronunciation is similar to the 'ı' in Turkish.

## Installation

```bash
pip install arabic-phonetiser
```

## Usage

Here is a simple example:

```python
import arabic_phonetiser

arabic_text = "أگُلّـچْ يَبـنْتي وأَسَمْعـچْ يَچَنْتي"
phon_text = arabic_phonetiser.arabic_to_phonemes(arabic_text)
print(phon_text)
```

Output:

```
< a G u ll ı C + y a b ı n t ii + uu < a s a m E ı C + y a C a n t ii
```

## License

This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License. The original work is by Nawar Halabi. For the full license text, please see the LICENSE file in the repository.

## Acknowledgements

This work is a fork of [Nawar Halabi's Arabic-Phonetiser](https://github.com/nawarhalabi/Arabic-Phonetiser). Special thanks to Nawar Halabi for the original work.
