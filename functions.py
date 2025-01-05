# Defines functions for spelling bee solver
# 01/04/2025
# Nico Dellario


import classes


def getLetters(word):
    letters = set()
    for i in range(len(word)):
        letters.add(word[i])
    return letters


def getPuzzle():
    mainLetter = input("Main letter: ").lower()
    otherLetters_str = input("Other letters separated by spaces: ").lower()
    otherLetters = set(otherLetters_str.split())
    puzzle = classes.Puzzle(mainLetter, otherLetters)
    return puzzle


def getDictionary():
    dictionary_file = open("english_dictionary.txt", "r")
    dictionary_txt = dictionary_file.read()
    dictionary = dictionary_txt.split()
    return dictionary


def convertToWordClass(words):
    word_list = set()
    for word in words:
        new_word = classes.Word(word)
        word_list.add(new_word)
    return word_list


def getMainWords(puzzle, dictionary):  # finds words in dictionary with main letter
    main_words = list()
    for word in dictionary:
        if puzzle.mainLetter in word.letters:
            main_words.append(word)
    return main_words


def hasValidLetters(word, puzzle_letters):
    # checks if every letter in word fits the available letters
    for letter in word.letters:
        if not letter in puzzle_letters:
            return False
    return True


def getValidWords(puzzle, main_word_list, min_letter_count):
    valid_words = set()
    for word in main_word_list:
        if len(word.word) >= min_letter_count and hasValidLetters(word, puzzle.allLetters):
            valid_words.add(word.word)
    return valid_words



        