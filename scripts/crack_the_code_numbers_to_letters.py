import itertools
from collections import Counter

the_code = "18 5 22 25 15 5 17 13  18 19  23 25 15 19 23 12 13   24 19 3 19 17 13 24 9  23 5 23 12 13  15 25 17 19 22 13  5 17 9      17 19  10 25 22 5 18 25   15 5   15 13 17 13     1 19   24 19 8 19 17 9 17 25"
dictionary_file_path = r"C:\Users\slawo\Downloads\sjp-20200205\slowa.txt"


# read dictionary file with all possible words
print ("read dictionary")
dictionary_file = open(dictionary_file_path, "r")
dictionary = dictionary_file.read()
words_in_dictionary = dictionary.replace("\n"," ").split(" ")



# initial parser of the code
print ("initialize parser")
words = [str(x).strip() for x in the_code.split("  ") if len(str(x).strip()) > 1 ]
words_in_code = dict()
for word in words:
    words_in_code[word] = dict()
    words_in_code[word]["text"] = word
    words_in_code[word]["length"] = len(word.split(' '))
    words_in_code[word]["words_a_len"] = len([x for x in words_in_dictionary if len(x) == words_in_code[word]["length"]])
    words_in_code[word]["words_a"] = [x for x in words_in_dictionary if len(x) == words_in_code[word]["length"]]







# 1 - simple, check repeating characters in specific places and check matching words
print ("simple check / occurences")
for key, value in words_in_code.items():

    tmp_list_of_possible_words = list(value["words_a"])
    new_tmp_list_of_possible_words = []

    current_word = value["text"]
    list_of_occurences = Counter(current_word.split(" "))
    list_of_repeating = [k for k, v in list_of_occurences.items() if int(v) > 1]

    if len(list_of_repeating) > 0:

        iteration = 1
        for code in list_of_repeating:

            indexes = [i for i,n in enumerate(current_word.split(" ")) if n == code]

            for possible_word in tmp_list_of_possible_words:

                temp_characters = []

                for index in indexes:
                    temp_characters.append(possible_word[index])

                if len(set(temp_characters)) == 1:
                    new_tmp_list_of_possible_words.append(possible_word)

            tmp_list_of_possible_words = new_tmp_list_of_possible_words
            
            if iteration != len(list_of_repeating):
                new_tmp_list_of_possible_words = []
                iteration = iteration + 1


        words_in_code[current_word]["words_b_len"] = len(new_tmp_list_of_possible_words)
        words_in_code[current_word]["words_b"] = new_tmp_list_of_possible_words
    else:
        words_in_code[current_word]["words_b_len"] = len(tmp_list_of_possible_words)
        words_in_code[current_word]["words_b"] = tmp_list_of_possible_words






# generate all possible pairs of words
print ("generate combinations")
all_words_combinations = list(set(itertools.combinations(words, 2)))



# # crack...
print ("crack")
iteration_combination = 1
for combination in all_words_combinations:

    print("crack combination " + str(iteration_combination) + " of " + str(len(all_words_combinations)) + "     >>      " + str(combination))


    words_in_code[combination[0]]["words_c_len"] = words_in_code[combination[0]]["words_b_len"]
    words_in_code[combination[0]]["words_c"] = words_in_code[combination[0]]["words_b"]
    words_in_code[combination[1]]["words_c_len"] = words_in_code[combination[1]]["words_b_len"]
    words_in_code[combination[1]]["words_c"] = words_in_code[combination[1]]["words_b"]



    list_of_combination_a = str(combination[0]).split(" ")
    list_of_combination_b = str(combination[1]).split(" ")
    common_codes = list(set(list_of_combination_a).intersection(list_of_combination_b))
        
    tmp_list_of_possible_words_a = words_in_code[combination[0]]["words_c"]
    new_tmp_list_of_possible_words_a = []
    tmp_list_of_possible_words_b = words_in_code[combination[1]]["words_c"]
    new_tmp_list_of_possible_words_b = []
    
    if len(common_codes) > 0:

        for common_code in common_codes:


            indexes_of_a = [i for i,n in enumerate(list_of_combination_a) if n == common_code]
            indexes_of_b = [i for i,n in enumerate(list_of_combination_b) if n == common_code]

            iteration = 1
            for possible_word_a in tmp_list_of_possible_words_a:
                for possible_word_b in tmp_list_of_possible_words_b:

                    current_values_in_given_indexes_for_possible_word_a = [n for i,n in enumerate(possible_word_a) if i in indexes_of_a]
                    current_values_in_given_indexes_for_possible_word_b = [n for i,n in enumerate(possible_word_b) if i in indexes_of_b]
                    all_current_values_from_possible_a_and_b = current_values_in_given_indexes_for_possible_word_a + current_values_in_given_indexes_for_possible_word_b

                    if len(set(all_current_values_from_possible_a_and_b)) == 1:
                        if possible_word_a not in new_tmp_list_of_possible_words_a:
                            new_tmp_list_of_possible_words_a.append(possible_word_a)
                        if possible_word_b not in new_tmp_list_of_possible_words_b:
                            new_tmp_list_of_possible_words_b.append(possible_word_b)

            tmp_list_of_possible_words_a = new_tmp_list_of_possible_words_a
            tmp_list_of_possible_words_b = new_tmp_list_of_possible_words_b

            if iteration != len(list_of_repeating):
                new_tmp_list_of_possible_words_a = []
                new_tmp_list_of_possible_words_b = []
                iteration = iteration + 1



            dadsa = 3



        dsadsa = 453

        words_in_code[combination[0]]["words_c_len"] = len(new_tmp_list_of_possible_words_a)
        words_in_code[combination[0]]["words_c"] = new_tmp_list_of_possible_words_a
        words_in_code[combination[1]]["words_c_len"] = len(new_tmp_list_of_possible_words_b)
        words_in_code[combination[1]]["words_c"] = new_tmp_list_of_possible_words_b
    
    else:
        words_in_code[combination[0]]["words_c_len"] = len(tmp_list_of_possible_words_a)
        words_in_code[combination[0]]["words_c"] = tmp_list_of_possible_words_a
        words_in_code[combination[1]]["words_c_len"] = len(tmp_list_of_possible_words_b)
        words_in_code[combination[1]]["words_c"] = tmp_list_of_possible_words_b

    iteration_combination = iteration_combination + 1






for key, value in words_in_code.items():
    x = str(value["text"])
    y0 = str(len(words_in_dictionary))
    y1 = str(value["words_a_len"])
    y2 = str(value["words_b_len"])
    y2 = str(value["words_c_len"])
    print (x + " : " + y0 + "   >   " + y1 + "  >   " + y2 + "  >   " + y2)