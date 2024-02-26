import argparse
import os
import time

from WordleGame import Wordle
from Strategies import HModeSimple
from Strategies import NModeMaximizeEntropy
from Strategies import NModeMaximizeEntropyCommon
from Strategies import HModeMaximizeEntropyCommon
from Strategies import HModeMaximizeEntropy
from Strategies import HModeSimpleCommon
import sys

# or other long operations

current_directory = os.getcwd()
wordleanswers = open("Wordlists/wordle_answers", "r")
words_to_list = wordleanswers.read().split("\n")
wordleanswers.close()

parser = argparse.ArgumentParser()
parser.add_argument('options', type=str, help='Mode')
parser.add_argument('mode', type=str, help='mode of wordle game')
command = parser.parse_args()

option = command.options
mode = command.mode


def benchmark(mode, algorithm):
    Total_Attempts = 0
    Words_Solved = 0
    Words_Not_Solved = 0
    List_Words_Not_Solved = []

    for word in words_to_list:
        sys.stdout.write("\rCompleted: %d/%d" % (Words_Solved, len(words_to_list)))
        game = Wordle(word, algorithm, mode)
        game.benchmark()

        Total_Attempts += game.ATTEMPTS

        if game.ATTEMPTS > 6:
            Words_Not_Solved += 1
            List_Words_Not_Solved.append(word)
        else:
            Words_Solved += 1
        bar = ''
        bar += "\u2588"

        sys.stdout.flush()

    Average_attempt = Total_Attempts / len(words_to_list)
    print("\nAverage: " + str(Average_attempt))
    print("Solved: " + str(Words_Solved))
    print("Words solved above 6 tries: " + str(Words_Not_Solved))
    print(List_Words_Not_Solved)


def solve(mode, algorithm):
    game = Wordle('', algorithm, mode)
    game.solve_wordle('salet')


if __name__ == "__main__":

    if option == "benchmark":
        if mode == "HARD":
            algorithm = HModeMaximizeEntropyCommon
            benchmark(mode, algorithm)
        if mode == "NORMAL":
            algorithm = NModeMaximizeEntropyCommon
            benchmark(mode, algorithm)
        else:
            raise Exception("Invalid Mode")

    elif option == "solve":
        if mode == "HARD":
            algorithm = HModeMaximizeEntropyCommon
            solve(mode, algorithm)
        if mode == "NORMAL":
            algorithm = NModeMaximizeEntropyCommon
            solve(mode, algorithm)
        else:
            raise Exception("Invalid Mode")
    else:
        raise Exception("Invalid program option")
