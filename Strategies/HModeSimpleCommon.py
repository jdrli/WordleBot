import random
import FilterPossibleWords

# Code base

def get_word(answer_input, word, common_words_list, all_words_list, uncertainty):

    optimizedList = FilterPossibleWords.analyze_result(word, answer_input, all_words_list)
    commonlist = FilterPossibleWords.list_with_common_words(optimizedList, common_words_list)
    if commonlist:
        startWord = random.choice(commonlist)

    else:
        startWord = random.choice(optimizedList)
    return startWord


