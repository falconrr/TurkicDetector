#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Program to identify language of a given string
"""

import fasttext
fasttext.FastText.eprint = lambda x: None # ignore warning

class LanguageIdentification:
    """
    Class object for Language Identification
    """

    def __init__(self):
        """
        Initializing class objects
        """
        pretrained_lang_model = "lid.176.bin"
        self.model = fasttext.load_model(pretrained_lang_model)

    def predict_lang(self, text):
        """
        Attributes
        text: type str, the sentence for which language is to be identified
        """
        predictions = self.model.predict(text, k=1) # top 1 matching languages
        return predictions

sent = input("Please type here your word or sentence in a Turkic language: ", )
if __name__ == '__main__':
    LANGUAGE = LanguageIdentification()
    LANG = LANGUAGE.predict_lang(str(sent))
    LANG = list(LANG) # make a list
    LANGL = str(LANG[0]) # create a string for the label so you can delete the '__label__'
    LANGL = LANGL.replace('__label__', '') # deleting __label__
    LANGL = str(LANGL) # now returning to string
# if statements to simplify the labeling of the Turkic language
if "tr" in LANGL:
    print("The language is: Turkish")
elif "cv" in LANGL:
    print("The language is: Chuvash")
elif "kk" in LANGL:
    print("The language is: Kazakh")
elif "az" in LANGL:
    print("The language is: Azerbaiijani")
elif "ug" in LANGL:
    print("The language is: Uyghur")
elif "ba" in LANGL:
    print("The language is: Bashkir")
elif "ky" in LANGL:
    print("The language is: Kyrgyz")
elif "tk" in LANGL:
    print("The language is: Turkmen")
else:
    print(LANGL)
# printing nicely the probability
for x in LANG[1]:
    print("Probability:", x)
