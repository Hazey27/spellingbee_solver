# Script finds words that can be made with the NYT spelling bee
# User enters mauin letter, then following letters and script queries dictionary for words that contain those letters
# 01/04/2025
# Nico Dellario


# import os, sys
# print(os.path.dirname(sys.executable))


import functions


# Variable for minimum number of letters a word must have for it to count in spelling bee
min_letter_count = 4


# Get puzzle from user
puzzle = functions.getPuzzle()

str_dict = functions.getDictionary()  # gets list of words from english_dictionary.txt
word_dict = functions.convertToWordClass(str_dict)  # turn list of words into set of word objects

main_words = functions.getMainWords(puzzle, word_dict)
valid_words = functions.getValidWords(puzzle, main_words, min_letter_count)

print(sorted(list(valid_words)))
