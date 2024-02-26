import random


# Methods

def filter_words_no_letter(wordList, letter):
    emptyList = []
    for everyword in wordList:

        if letter not in everyword:
            emptyList.append(everyword)
    return emptyList


def filter_words_with_letter(wordList, letter):
    emptyList = []
    for everyword in wordList:
        if letter in everyword:
            emptyList.append(everyword)
    return emptyList



def filter_words_wrong_position(wordList, index, letter):
    emptyList = []
    for everyword in wordList:
        if letter != everyword[index]:
            emptyList.append(everyword)
    return emptyList

def filter_words_correct_position(wordList, index, letter):
    emptyList = []
    for everyword in wordList:
        if letter == everyword[index]:
            emptyList.append(everyword)
    return emptyList



def contains_duplicate_letter(word, index):
    for i in range(len(word)):
        if i != index and word[i] == word[index]:
            return True
    return False


def grey_all_duplicates(word, letter, index, userinput):
    for i in range(5):
        if word[i] == letter and userinput[i] != '0':
            return False
    return True

def list_with_common_words(optimizedlist, list):
    emptylist = []
    for word in optimizedlist:
        if word in list:
            emptylist.append(word)
    return emptylist



def analyze_result(wordUsed, userInput, wordList):
    index = 0


    for element in userInput:
        emptylist = []
        if element == '0':
            if not contains_duplicate_letter(wordUsed, index):
                newlist = filter_words_no_letter(wordList, wordUsed[index])
                for newword in newlist:
                    emptylist.append(newword)
            else:
                if grey_all_duplicates(wordUsed, wordUsed[index], index, userInput):
                    newlist = filter_words_no_letter(wordList, wordUsed[index])
                    for newword in newlist:
                        emptylist.append(newword)
                else:
                    newlist = filter_words_wrong_position(wordList, index, wordUsed[index])
                    for newword in newlist:
                        emptylist.append(newword)
        if element == '1':
            newlist = filter_words_with_letter(wordList, wordUsed[index])
            for newword in newlist:
                emptylist.append(newword)

            newsecondlist = filter_words_wrong_position(emptylist, index, wordUsed[index])
            emptylist.clear()
            for posiword in newsecondlist:
                emptylist.append(posiword)


        if element == '2':
            newlist = filter_words_correct_position(wordList ,index, wordUsed[index])
            for newword in newlist:
                emptylist.append(newword)

        wordList.clear()
        for everyword in emptylist:
            wordList.append(everyword)


        index += 1
    return wordList


def get_word_with_most_recurring_letter(optimizedlist, letters_not_used):

    emptylist = []
    letter_number = 0
    for letter in letters_not_used:
        list_of_words_with_letter = []
        for word in optimizedlist:
            if letter in word:
                list_of_words_with_letter.append(word)
        if len(list_of_words_with_letter) >= letter_number:
            letter_number = len(list_of_words_with_letter)
            emptylist.append(letter)
    most_letter = emptylist[-1]
    for word in optimizedlist:
        if most_letter in word:
            return word
        else:
            return random.choice(optimizedlist)

def prioritize_unique_letters(optimizedlist):
    emptylist = []
    for words in optimizedlist:
        if len(set(words)) == len(words):
            emptylist.append(words)

    return emptylist
