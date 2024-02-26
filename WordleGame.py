import math
import os
import re

import FilterPossibleWords

current_directory = os.getcwd()

commonwords = open("Wordlists/commonwords_with_answers", "r")
allguessingwords = open("Wordlists/words.txt", "r")
words_to_list = allguessingwords.read().split("\n")
commonwords_to_list = commonwords.read().split("\n")
comb = open("Wordlists/output.txt", "r")
combination_list =comb.read().split("\n")
wordleanswers = open("Wordlists/wordle_answers", "r")
answer_list = wordleanswers.read().split("\n")



class Wordle:

    list_of_commonwords = []
    list_of_guessing_words = []
    list_of_answers = []

    for words in commonwords_to_list:
        list_of_commonwords.append(words)

    for words in words_to_list:
        list_of_guessing_words.append(words)

    for words in answer_list:
        list_of_answers.append(words)
    #RESULTS
    ATTEMPTS = 0



    def __init__(self, answer, wordleStrategy, mode):
        self.answer = answer
        self.strategy = wordleStrategy
        self.mode = mode

    def inputResult(self):
        while True:

            result = input('Result? ')
            if self.valid_result(result):
                return result
            else:
                print("Invalid result")

    def valid_result(self, result):
        if len(result) != 5:
            return False
        if not bool(re.match('^[012]+$', result)):
            return False
        return True

    def get_input_from_words(self, guess, correct_word):
        input = list('-----')
        answer = list(correct_word)
        index = 0
        for letter in guess:
            if letter == answer[index]:
                input[index] = '2'
                answer[index] = '-'
            else:
                if letter in answer:
                    input[index] = '1'
                else:
                    input[index] = '0'
            index += 1
        return ''.join(input)

    def reset_lists(self):

        self.list_of_commonwords.clear()
        self.list_of_guessing_words.clear()
        self.list_of_answers.clear()
        self.list_of_commonwords.extend(commonwords_to_list)
        self.list_of_guessing_words.extend(words_to_list)
        self.list_of_answers.extend(answer_list)

    def retrieve_bin(self, input):
        for comb in combination_list:
            if input in comb:
                # using split()
                # Get String after substring occurrence
                res = comb.split('=', 1)
                splitString = res[1].replace(" ", "")
                return splitString

    def benchmark(self):
        information = 13.66
        guess = 'salet'
        input = self.get_input_from_words(guess, self.answer)
        optimizedList = FilterPossibleWords.analyze_result(guess, input, self.list_of_guessing_words)
        probability = 1/len(optimizedList)
        salet_information = 13.66 - math.log(1/probability, 2)
        uncertainty = 13.66 - salet_information


        self.ATTEMPTS += 1
        while input != '22222':
            if self.ATTEMPTS == 1 and self.mode == "NORMAL":
                self.ATTEMPTS +=1

                guess = self.retrieve_bin(input)
                input = self.get_input_from_words(guess, self.answer)
                optimizedList = FilterPossibleWords.analyze_result(guess, input, self.list_of_guessing_words)
                probabilitytwo = 1 / len(optimizedList)
                second_information = uncertainty - math.log(1/probabilitytwo, 2)
                uncertainty = uncertainty - second_information

            else:

                guess = self.strategy.get_word(input, guess, commonwords_to_list, optimizedList, uncertainty)
                # Get input answer from guess
                input = self.get_input_from_words(guess, self.answer)
                self.ATTEMPTS += 1
                probabilityrepeat = 1 / len(optimizedList)
                repeat_information = uncertainty - math.log(1 / probabilityrepeat, 2)
                uncertainty = uncertainty - repeat_information


        self.reset_lists()



    def solve_wordle(self, first_guess):
        print("Guess with word: salet")
        input = self.inputResult()
        guess = first_guess
        self.ATTEMPTS +=1
        optimizedList = FilterPossibleWords.analyze_result(guess, input, self.list_of_guessing_words)
        probability = 1 / len(optimizedList)
        salet_information = 13.66 - math.log(1 / probability, 2)
        uncertainty = 13.66 - salet_information

        while input != '22222':



            if self.ATTEMPTS == 1 and self.mode == "NORMAL":
                self.ATTEMPTS += 1
                guess = self.retrieve_bin(input)
                print("Guess with word:" + guess)
                input = self.inputResult()
                optimizedList = FilterPossibleWords.analyze_result(guess, input, self.list_of_guessing_words)
                probabilitytwo = 1 / len(optimizedList)
                second_information = uncertainty - math.log(1 / probabilitytwo, 2)
                uncertainty = uncertainty - second_information
            else:
                self.ATTEMPTS += 1

                guess = self.strategy.get_word(input, guess, commonwords_to_list, optimizedList, uncertainty)
                probabilityrepeat = 1 / len(optimizedList)
                repeat_information = uncertainty - math.log(1 / probabilityrepeat, 2)
                uncertainty = uncertainty - repeat_information
                print("Guess with word:" + guess)
                input = self.inputResult()



        self.reset_lists()






