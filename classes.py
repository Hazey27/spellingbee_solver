# Defines word class with attributes word and letters
# 01/04/2025
# Nico Dellario


import functions


class Word:
    def __init__(self, word):
        self.word = word
        self.letters = functions.getLetters(word)


class Puzzle:
    def __init__(self, mainLetter, otherLetters):
        self.mainLetter = mainLetter
        allLetters = set(mainLetter)
        allLetters.update(otherLetters)
        self.allLetters = allLetters


# Testing class and getLetters() function

# myword = "supercalifragalisticexpialadocious"

# myword = word(myword)
# print(str(myword.letters) + ", " + str(myword.word))










