# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:04:27 2019

@author: timil
"""

def main():

   mystr = raw_input("Enter your String:")
   mystr.lower()
   vowelSet = set(['a','e','i','o','u'])


   runVowels(mystr, vowelSet)
   runConsonants(mystr, vowelSet)

def runVowels(mystr, vowelSet):
    #index, vowels needs to be defined
    index = 0
    vowels = 0

    while index < len(mystr):
        if mystr[index] in vowelSet:
            vowels += 1

        # You need to increment index outside of the condition
        index += 1
print ('This string consists of ', vowels , 'vowels')

def runConsonants(mystr, vowelSet):
    index = 0
    consonants = 0
    while index < len(mystr):
        if mystr[index] not in vowelSet:
            consonants += 1
print ('This string consists of ', consonants , 'consonants')
