# A language detector for Turkic languages

This repo contains a code optimized to detect Turkic languages from a given text in python using Facebook's library [fasttext](https://fasttext.cc/docs/en/language-identification.html).

# Quickstart

### Requirements

  -  $ pip3 install fasttext
  - Download in the same directory: [lid.176.bin](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin). This is the faster and more accurate version of the language identification tool.  

### How to run
To simply use code use `TurkicDetector.py`. $ python3 TurkicDetector.py

The python code has been adapted to be more user friendly for users looking to identify a Turkic language. Fasttext has pretrained word vectors for 10 Turkic languages, including: Turkish, Kazakh, Azerbaijani, Chuvash, Tatar, Uyghur, Uzbek, Bashkir, Kyrgyz, and Turkmen

This program uses the binary file [lid.176.bin](https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin) for high accuracy (126 MB).

### License

- `TurkicDetector` is a public domain work, dedicated using
[CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

- Adapted from c-chaitanya (https://github.com/c-chaitanya/language-identification)
