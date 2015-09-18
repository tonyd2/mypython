# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 18:06:45 2015

@author: Tony
Description: Pull etext numbers from Project Gutenberg for an author

1) First pip install gutenberg 0.4.0 library for Python from the command line

"""
 
from gutenberg.query import get_etexts
from gutenberg.query import get_metadata
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers


# get the catalogue numbers of all the texts
# by Wilhelm Grimm in Project Gutenberg
bookList=get_etexts('author', 'Grimm, Wilhelm Carl')
# gives bookList = [12704, 12705, 12706, 12707, 12708, 12709, 12710, 37381, 20051, 28044, 30510, 22555, 20050, 11027, 16846, 12250, 20027, 19068, 2591]

#Once We can associate a number with a title we can pull the text
for number in bookList:
    print(number,get_metadata('title',number))
 
print('\n HHHHHHHHHHHHHHH Now for the full text HHHHHHHHHHHHHHHHHHH \n')
# Once we have the text number we can print the text
# example 11027 is the number for Grimm's Fairy Stories 
# can be tempermental truncating text at top (console limit?) may need to trick around  
etext = strip_headers(load_etext(11027)).strip()
print(etext)