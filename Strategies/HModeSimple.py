import random
import FilterPossibleWords

# Code base

def get_word(answer_input, word, common_words_list, all_words_list, uncertainty):

    optimizedList = FilterPossibleWords.analyze_result(word, answer_input, all_words_list)
    startWord = random.choice(optimizedList)

    return startWord
