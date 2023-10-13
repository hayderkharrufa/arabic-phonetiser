from setuptools import setup, find_packages

setup(
    name='arabic_phonetiser',
    version='1.0.5',
    packages=find_packages(),
    install_requires=[
        "arabic_buckwalter_transliteration"
    ],
    license='Creative Commons Attribution-NonCommercial 4.0 International License',
    url='https://github.com/hayderkharrufa/arabic-phonetiser',
    author='Hayder Kharrufa',
    author_email='',
)