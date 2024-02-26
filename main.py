import argparse
import os
import time
from webscrape import webscraper
from WordleGame import Wordle
from Strategies import NModeMaximizeEntropy
from Strategies import NModeMaximizeEntropyCommon
import sys

current_directory = os.getcwd()
wordleanswers = open("Wordlists/wordle_answers", "r")
words_to_list = wordleanswers.read().split("\n")
wordleanswers.close()
mode = "NORMAL"

def solve(mode, algorithm):
    game = Wordle('', algorithm, mode)
    game.solve_wordle('salet')

# attempts = int(input("How many attempts would you like to iterate through? \n"))
webscraper.openwordle()
algorithm = NModeMaximizeEntropyCommon
solve(mode, algorithm)
input("Press enter to close browser...")
