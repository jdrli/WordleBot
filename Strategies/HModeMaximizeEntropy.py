
import FilterPossibleWords
import math




def get_input_from_words(guess, correct_word):
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


def get_word(answer_input, word, common_words_list, words_to_list, uncertainty):

    optimizedList = FilterPossibleWords.analyze_result(word, answer_input, words_to_list)



    if len(optimizedList) == 1:


        return optimizedList[0]
    empty_list = []
    empty_list.extend(optimizedList)

    highest_entropy_words = []

    entropy = 0

    for word in optimizedList:

        information = get_expected_max_entropy(word, optimizedList)
        optimizedList.clear()
        optimizedList.extend(empty_list)

        if information > entropy:

            entropy = information
            highest_entropy_words.append(word)


    return highest_entropy_words[-1]

def get_expected_max_entropy(word, optimized_list):

    previous_size = len(optimized_list)
    empty_list = []
    empty_list.extend(optimized_list)

    added_bits = 0


    for optimize_word in optimized_list:

        input = get_input_from_words(word, optimize_word)
        new_list_size = len(FilterPossibleWords.analyze_result(word, input, optimized_list))

        probability = new_list_size/previous_size
        optimized_list.clear()
        optimized_list.extend(empty_list)

        if probability != 0:

            added_bits += math.log(1/probability, 2)

    expected_information = added_bits/len(empty_list)

    return expected_information

