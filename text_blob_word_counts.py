# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 18:44:43 2015

@author: Tony
"""
from textblob import TextBlob

# function to check for each punctuation item in list and replace with nothing
def remove_punc(text):
    punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'
    for marker in punctuation:
        text = text.replace(marker, "")
    return text
# The four variant fairy tales are kept in the folder called 'texts':
# the_king_of_erin_and_the_queen_of_the_lonesome_isle.txt
# the_brown_bear_from_the_green_glen.txt
# the_king_of_england_and_his_three_sons.txt
# the_water_of_life.txt
infile = open('texts/the_water_of_life.txt')
tale = infile.read()
infile.close()

#make file all lower case as punctuation irregular in some tales
tale_lwr=tale.lower()
#remove all punctuation and strange symbols
tale_text = remove_punc(tale_lwr)

textToAnalyse = TextBlob(tale_text)
#Scottish
#Irish
#English  0 1 3 0
#German
word_list = ['curse','spell','sleep','food','eat','drink','iron','bear']
phrase_list = ['eat and drink']

for word in word_list:
    print(word,textToAnalyse.words.count(word))
for phrase in phrase_list:
    print(phrase,textToAnalyse.noun_phrases.count('eat and drink')) 



                   
