"""S1 2018 Assignment 4 Questions - This program MUST be used for testing
the functions of assignment 4
"""

def main():
    user_selection = 1
    while user_selection >= 1 and user_selection <= 8:
        print()
        user_selection = get_user_selection()
        print()
        if user_selection == 1:
            print_header(user_selection, "test_draw_histogram()")
            test_draw_histogram()
        elif user_selection == 2:
            print_header(user_selection, "test_get_word_len_dict()")
            test_get_word_len_dict()
        elif user_selection == 3:
            print_header(user_selection, "test_get_text_valuation()")
            test_get_text_valuation()
        elif user_selection == 4:
            print_header(user_selection, "test_remove_short_synonyms()")
            test_remove_short_synonyms()
        elif user_selection == 5:
            print_header(user_selection, "test_get_triples_dict()")
            test_get_triples_dict()
        elif user_selection == 6:
            print_header(user_selection, "test_contains_keys_and_values()")
            test_contains_keys_and_values()
        elif user_selection == 7:
            print_header(user_selection, "test_get_previous_words_dict()")
            test_get_previous_words_dict()
        print()

def get_user_selection():
    print('   1. test_draw_histogram():')
    print('   2. test_get_word_len_dict():')
    print('   3. test_get_text_valuation():')
    print('   4. test_remove_short_synonyms():')
    print('   5. test_get_triples_dict():')
    print('   6. test_contains_keys_and_values():')
    print('   7. test_get_previous_words_dict():')
    print('   0. Quit: ')
    return int(input("      Enter selection: "))
#--------------------------------------------------
# 7777777777777777777777777777777777777777777777777
# get_previous_words_dict()
#--------------------------------------------------
#--------------------------------------------------
"""
Define the get_previous_words_dict() function which is passed a string
of text as a parameter. The function returns a dictionary with keys
which are all the unique words from the text, and corresponding values
which are lists of all the unique words in the text which come before
the key word. Note that in each corresponding list of previous words,
the same word should not appear more than once.

Notes:
鈥� the first word in the sentence will initially have the empty string
as its previous word,
鈥� you can assume that the text is all in lower case and contains no
punctuation,
鈥� each list of previous words must be sorted into ascending order,
鈥� the testing code makes use of the print_dict_in_key_order(a_dict)
which prints the dictionary pairs in sorted key order.

For example, the following code:

text = 'a man we saw saw a saw'
previous_words_dict = get_previous_words_dict(text)
print_dict_in_key_order(previous_words_dict)
print()

text = 'my favourite painting is the painting i did of my dog in that painting in my den'
previous_words_dict = get_previous_words_dict(text)
print_dict_in_key_order(previous_words_dict)

prints:

a : ['', 'saw']
man : ['a']
saw : ['a', 'saw', 'we']
we : ['man']

den : ['my']
did : ['i']
dog : ['my']
favourite : ['my']
i : ['painting']
in : ['dog', 'painting']
is : ['painting']
my : ['', 'in', 'of']
of : ['did']
painting : ['favourite', 'that', 'the']
that : ['in']
the : ['is']
"""
def get_previous_words_dict(text):
    text_list = text.split()
    a_dict = {}
    text_list.insert(0, "")
    a_list = []
    for word in text_list:
        if word not in a_list:
            a_list += [word]
    a_list.sort()
    for word2 in a_list:
        a_dict[word2] = []
    for index in range(len(text_list)):
        if text_list[index] not in a_dict:
            a_dict[text_list[index]] = [text_list[index-1]]
        else:
            a_dict[text_list[index]] += [text_list[index-1]]
    all_keys = list(a_dict.keys())
    all_keys.sort()
    for key in all_keys:
        a_dict[key].sort()
        if key == "":
            del a_dict[key]
    return a_dict



def test_get_previous_words_dict():
    sentence = 'a man we saw saw a saw'
    previous_words_dict = get_previous_words_dict(sentence)
    print_dict_in_key_order(previous_words_dict)
    print()

    sentence = 'my favourite painting is the painting i did of my dog in that painting in my den'
    previous_words_dict = get_previous_words_dict(sentence)
    print_dict_in_key_order(previous_words_dict)
#--------------------------------------------------
# 6666666666666666666666666666666666666666666666666
# contains_keys_and_values()
#--------------------------------------------------
"""
Define the contains_keys_and_values() function which is passed two dict
objects as parameters, dict1 and dict2. The two parameter dictionaries
both have corresponding values which are lists of elements (numbers or
strings).  The function return True if the following two conditions are
met:

鈥� dict1 contains all the keys which are in dict2 (dict1 may also contain
extra keys),
and,
鈥� the elements in all the value lists of dict2 are also elements in at
least one of the value lists of dict1.  Note: when testing this part of
the condition, the elements can be in any order and in any of the value
lists, e.g., if one of the values lists of dict2 is [4, 2] and any one
of the value lists of dict1 contains the element 4 and any one of the
value lists of dict1 contains the element 2, this part of the condition
is satisfied.

The function returns False in all other cases.

For example, the following code:
 
dict1 = {}
dict2 = {}
print("1.", contains_keys_and_values(dict1, dict2))

dict1 = {"a": [4, 3] , "d": [6, 2], "z": [], "t": [2, 23]}
dict2 = {"z": [2, 3, 6, 23], "a": [4]}
print("2.", contains_keys_and_values(dict1, dict2))

dict1 = {"a": [6, 3], "p": []}
dict2 = {"a": [3, 6, 3], "p": [6, 1]}
print("3.", contains_keys_and_values(dict1, dict2))

dict1 = {"a": [6, 3], "p": []}
dict2 = {"a": [3, 6, 3], "p": ['a']}
print("4.", contains_keys_and_values(dict1, dict2))

dict1 = {"a": [6, 3], "p": ['a'], "t": ['s']}
dict2 = {"a": [3, 6, 3], "p": ['a'], "s": ['a']}
print("5.", contains_keys_and_values(dict1, dict2))


prints:

1. True
2. True
3. False
4. False
5. False
"""
def contains_keys_and_values(dict1, dict2):
    a_list = []
    b_list = []
    c_list = []
    k1_list = []
    k2_list = []
    for num in list(dict2.values()):
        for value in range(len(num)):
            a_list += [num[value]]
    for number in list(dict1.values()):
        for element in range(len(number)):
            b_list += [number[element]]
    for key2 in list(dict2.keys()):
        for key4 in range(len(key2)):
            k2_list += [key2[key4]]
    for key1 in list(dict1.keys()):
        for key3 in range(len(key1)):
            k1_list += [key1[key3]]
    for key4 in k2_list:
        if key4 in k1_list:
            c_list += [True]
        else:
            c_list += [False]
    for value1 in a_list:
        for element1 in b_list:
            if value1 == element1 == "":
                c_list += [True]
            elif value1 in b_list:
                c_list += [True]
            else:
                c_list += [False]
    if False in c_list:
        return False
    else:
        return True
    
def test_contains_keys_and_values():
    dict1 = {}
    dict2 = {}
    print("1.", contains_keys_and_values(dict1, dict2))

    dict1 = {"a": [4, 3] , "d": [6, 2], "z": [], "t": [2, 23]}
    dict2 = {"z": [2, 3, 6, 23], "a": [4]}
    print("2.", contains_keys_and_values(dict1, dict2))

    dict1 = {"a": [6, 3], "p": []}
    dict2 = {"a": [3, 6, 3], "p": [6, 1]}
    print("3.", contains_keys_and_values(dict1, dict2))

    dict1 = {"a": [6, 3], "p": []}
    dict2 = {"a": [3, 6, 3], "p": ['a']}
    print("4.", contains_keys_and_values(dict1, dict2))
    
    dict1 = {"a": [6, 3], "p": ['a'], "t": ['s']}
    dict2 = {"a": [3, 6, 3], "p": ['a'], "s": ['a']}
    print("5.", contains_keys_and_values(dict1, dict2))
#--------------------------------------------------
# 5555555555555555555555555555555555555555555555555
# get_triples_dict()
#--------------------------------------------------
"""
Define the get_triples_dict() function which is passed a string of text
as a parameter. The function first converts the parameter string to
lower case and then returns a dictionary with keys which are all the
unique consecutive three alphabetic characters from the text, and the
corresponding values are the number of times the three consecutive
alphabetic characters appear in the text. Use the isalpha() method to
check if a character is alphabetic or not. The dictionary should only
contain entries which occur more than once.  After your dictionary has
been created and populated, you need to remove any key-value pairs which
have a corresponding value of 1. For example, if the text is "Super,
duper" the algorithm proceeds as follows:

Character 's':  String is "s", Dictionary is {}
Character 'u':  String is "su", Dictionary is {}
Character 'p':  String is "sup", change string to "up", {'sup': 1}
Character 'e':  String is "upe", change string to "pe", Dictionary is 
                           {'sup': 1, 'upe': 1}
Character 'r':  String is "per", change string to "er", Dictionary is 
                           {'sup': 1, 'upe': 1, 'per': 1}
Character ',':  String is "er", Dictionary is {'sup': 1, 'upe': 1, 'per': 1}
Character ' ':  String is "er", Dictionary is {'sup': 1, 'upe': 1, 'per': 1}
Character 'd':  String is "erd", change string to "rd", Dictionary is 
                           {'sup': 1, 'upe': 1, 'per': 1, 'erd': 1}
Character 'u':  String is "rdu", change string to "du",
                           {'sup': 1, 'upe': 1, 'per': 1, 'erd': 1, 'rdu': 1}
Character 'p':  String is "dup", change string to "up", Dictionary is 
                           {'sup': 1, 'upe': 1, 'per': 1, 'erd': 1, 'rdu': 1, 'dup': 1}
Character 'e':  String is "upe", change string to "pe", Dictionary is 
                           {'sup': 1, 'upe': 2, 'per': 1, 'erd': 1, 'rdu': 1, 'dup': 1}
Character 'r':  String is "per", change string to "er", Dictionary is 
                           {'sup': 1, 'upe': 2, 'per': 2, 'erd': 1, 'rdu': 1, 'dup': 1}
Remove all entries with a value of 1: {'upe': 2, 'per': 2}

For example, executing the following code:

print("1.")
print_dict_in_key_order(get_triples_dict('super, duper'))
print("\n2.")
print_dict_in_key_order(get_triples_dict("ABC ABC ABC"))
print("\n3.")
print_dict_in_key_order(get_triples_dict("Sometimes the smallest things make more room in your heart"))
print("\n4.")
print_dict_in_key_order(get_triples_dict("My favourite painting is the painting i did of my dog in that painting in my den"))

prints (output is shown here in four separate columsn):

1.          2.          3.          4.
per - 2     abc - 3     est - 2     ain - 3
upe - 2     bca - 2     sma - 2     epa - 2
            cab - 2                 gin - 2
                                    ing - 3
                                    int - 4
                                    myd - 2
                                    ngi - 3
                                    nti - 3
                                    pai - 3
                                    tin - 3
"""
def get_triples_dict(text):
    text = text.lower()
    a_list = text.split()
    a_dict = {}
    string = ""    
    for num in range(len(text)):
        if text[num].isalpha():
            string += str(text[num])
            if len(string) >= 3:
                string = string[-3:]
                if string in a_dict:
                    a_dict[string] += 1
                else:
                    a_dict[string] = 1
    for key, value in list(a_dict.items()):
        if value == 1:
            del a_dict[key]
    return a_dict
    
def test_get_triples_dict():
    print("1.")
    print_dict_in_key_order(get_triples_dict('super, duper'))
    print("\n2.")
    print_dict_in_key_order(get_triples_dict("ABC ABC ABC"))
    print("\n3.")
    print_dict_in_key_order(get_triples_dict("Sometimes the smallest things make more room in your heart"))
    print("\n4.")
    print_dict_in_key_order(get_triples_dict("My favourite painting is the painting i did of my dog in that painting in my den"))
#--------------------------------------------------
# 4444444444444444444444444444444444444444444444444
# remove_short_synonyms()
#--------------------------------------------------
"""
Define the remove_short_synonyms() function which is passed a dictionary
as a parameter.  The keys of the parameter dictionary are words and the
corresponding values are lists of synonyms (synonyms are words which
have the same or nearly the same meaning).  The function removes all the
synonyms which have less than 7 characters from each corresponding list
of synonyms.  As well, the function sorts each corresponding list of
synonyms. For example, the following code:

synonyms_dict = {'look' : ['gaze', 'see', 'glance', 'watch', 'peruse'],
    'put' : ['place', 'set', 'attach', 'keep', 'save', 'set aside', 'effect',
          'achieve', 'do', 'build'],
    'beautiful' : ['pretty', 'lovely', 'handsome', 'dazzling', 'splendid',
                'magnificent'],
    'slow' : ['unhurried', 'gradual', 'leisurely', 'late', 'behind',
           'tedious', 'slack'],
    'dangerous' : ['perilous', 'hazardous', 'uncertain']
    }
remove_short_synonyms(synonyms_dict)
print("1.")
print_dict_in_key_order(synonyms_dict)    
print()

synonyms_dict = {'come' : ['approach', 'advance', 'near', 'arrive', 'reach'],
    'show' : ['display', 'exhibit', 'present', 'note', 'point to', 'indicate',
          'explain', 'reveal', 'prove', 'demonstrate', 'expose'],
    'good' : ['excellent', 'fine', 'superior', 'wonderful', 'grand', 'superb',
'edifying'],
    'bad' : ['evil', 'immoral', 'wicked', 'rotten', 'contaminated', 'spoiled',
        'defective',  'substandard', 'faulty', 'improper', 'inappropriate']
}    
remove_short_synonyms(synonyms_dict)
print("2.")
print_dict_in_key_order(synonyms_dict)

prints:

1.
beautiful : ['dazzling', 'handsome', 'magnificent', 'splendid']
dangerous : ['hazardous', 'perilous', 'uncertain']
look : []
put : ['achieve', 'set aside']
slow : ['gradual', 'leisurely', 'tedious', 'unhurried']

2.
bad : ['contaminated', 'defective', 'immoral', 'improper', 'inappropriate', 'spoiled', 'substandard']
come : ['advance', 'approach']
good : ['edifying', 'excellent', 'superior', 'wonderful']
show : ['demonstrate', 'display', 'exhibit', 'explain', 'indicate', 'point to', 'present']
"""
def remove_short_synonyms(synonyms_dict):
    a_dict = {}
    a_list = list(synonyms_dict)
    a_list.sort()
    for letter in a_list:
        a_dict[letter] = []
    for list1 in synonyms_dict.values():
        for num in range(len(list1)-1, -1, -1):
            if len(list1[num]) < 7:
                list1.pop(num)
        list1.sort()
        a_dict[letter] += list1
        
    return a_dict

def test_remove_short_synonyms():
    synonyms_dict = {'look': ['gaze', 'see', 'glance', 'watch', 'peruse'],
       'put': ['place', 'set', 'attach', 'keep', 'save', 'set aside', 'effect', 'achieve', 'do', 'build'],
       'beautiful': ['pretty', 'lovely', 'handsome', 'dazzling', 'splendid', 'magnificent'],
       'slow': ['unhurried', 'gradual', 'leisurely', 'late', 'behind', 'tedious', 'slack'],
       'dangerous': ['perilous', 'hazardous', 'uncertain']
       }
    remove_short_synonyms(synonyms_dict)
    print("1.")
    print_dict_in_key_order(synonyms_dict)

    synonyms_dict = {'come': ['approach', 'advance', 'near', 'arrive', 'reach'],
       'show': ['display', 'exhibit', 'present', 'point to', 'indicate', 'explain', 'prove', 'demonstrate', 'expose'],
       'good': ['excellent', 'fine', 'superior', 'wonderful', 'grand', 'superb', 'edifying'],
       'bad': ['evil', 'immoral', 'wicked', 'contaminated', 'spoiled', 'defective',  'substandard', 'faulty', 'improper', 'inappropriate']
       }

    remove_short_synonyms(synonyms_dict)
    print("\n2.")
    print_dict_in_key_order(synonyms_dict)
#--------------------------------------------------
# 3333333333333333333333333333333333333333333333333
# get_text_valuation()
#--------------------------------------------------    
#--------------------------------------------------
"""
Define the get_text_valuation() function which is passed two parameters,
a dictionary and a string of text.  The keys of the parameter dictionary
are single letters and the corresponding values are integers (the value
of the key letter), e.g., {'b': 5, 'a': 6, 'c': 3}.  The function
returns the total valuation (an integer) of the string of text where:

鈥� if the letter from the text is a keyletter of the dictionary then its value is the integer corresponding to the letter in the dictionary.
鈥� any alphabetic characters from the text which are not in the dictionary are worth 1,
and,
鈥� all non alphabetic characters are worth 0 (use the isalpha() method to check if a character is alphabetic or not).

Notes:
鈥� you will need to change the text to lowercase before you work out the total value of the text,
鈥� you can assume that all the keys in the dictionary are lowercase characters.

For example, the following code:

letter_value_dict = {"r": 2, "s": 2, "h":4, "t":3, "m": 7, "g":4, "v":8}

letters = "BLAH" 1+1+1+4
print("1.", letters, "-", get_text_valuation(letter_value_dict, letters))

letters = 'thought provoking'
print("2.", letters, "-", get_text_valuation(letter_value_dict, letters))

letters = "too much month at the end of the money"
print("3.", letters, "-", get_text_valuation(letter_value_dict, letters))

prints:

1. BLAH - 7
2. thought provoking - 40
3. too much month at the end of the money - 70
"""
def get_text_valuation(letter_value_dict, text):
    a_list = text.split()
    a_dict = {}
    total = 0
    for word in a_list:
        for num in range(len(word)):
            if word[num].isalpha():
                if word[num] in a_dict:
                    a_dict[word[num]] += 1
                else:
                    a_dict[word[num]] = 1
    for key in a_dict:
        if key.lower().isalpha():
            if key.lower() in letter_value_dict:
                total += (letter_value_dict[key.lower()]) * a_dict[key]
            else:
                total += 1 * a_dict[key]
        else:
            total += 0 * a_dict[key] 
    return total

def test_get_text_valuation():
    letter_value_dict = {"r": 2, "s": 2, "h": 4, "t": 3, "m": 7, "g": 4, "v": 8}
    letters = "BLAH"
    print("1.", letters, "-", get_text_valuation(letter_value_dict, letters))

    letters = 'thought provoking'
    print("2.", letters, "-", get_text_valuation(letter_value_dict, letters))

    letters = "too much month at the end of the money"
    print("3.", letters, "-", get_text_valuation(letter_value_dict, letters))
#--------------------------------------------------
# 2222222222222222222222222222222222222222222222222
# get_word_len_dict()
#--------------------------------------------------
"""
Define the get_word_len_dict() function which is passed a string of text
as a parameter.  The function returns a dictionary with keys which are
integers and corresponding values which are lists of unique words.  The
list of words corresponding to a key contains all the unique words from
the text that have a length equal to the key value.  The corresponding
lists of unique words should be in sorted alphabetical order.

Note: the testing code makes use of the print_dict_in_key_order(a_dict)
which prints the dictionary pairs in sorted key order.

For example, the following code:

text = "May your coffee be strong and your Monday be short"
the_dict = get_word_len_dict(text)
print_dict_in_key_order(the_dict)
print()

text = 'why does someone believe you when you say there are four billion stars but they have to check when you say the paint is wet'
the_dict = get_word_len_dict(text)
print_dict_in_key_order(the_dict)

prints:

2 : ['be']
3 : ['May', 'and']
4 : ['your']
5 : ['short']
6 : ['Monday', 'coffee', 'strong']

2 : ['is', 'to']
3 : ['are', 'but', 'say', 'the', 'wet', 'why', 'you']
4 : ['does', 'four', 'have', 'they', 'when']
5 : ['check', 'paint', 'stars', 'there']
7 : ['believe', 'billion', 'someone']
"""
def get_word_len_dict(text):
    my_list = text.split()
    a_list = []
    a_dict = {}
    for word in my_list:
        if len(word) not in a_list:
            a_list += [len(word)]
    for num in a_list:
        a_dict[num] = []
    for word1 in my_list:
        for num1 in a_list:
            if len(word1) == num1:
                if word1 not in a_dict[num1]:
                    a_dict[num1] += [word1]
    for value in a_dict.values():
        value.sort()
    return a_dict

def test_get_word_len_dict():
    text = "May your coffee be strong and your Monday be short"
    the_dict = get_word_len_dict(text)
    print_dict_in_key_order(the_dict)
    print()

    text = 'why does someone believe you when you say there are four billion stars but they have to check when you say the paint is wet'
    the_dict = get_word_len_dict(text)
    print_dict_in_key_order(the_dict)
#--------------------------------------------------
# 1111111111111111111111111111111111111111111111111
# draw_histogram()
#--------------------------------------------------
#--------------------------------------------------
"""
Define the draw_histogram() function which is passed a Python dictionary
as a parameter. The keys of the dictionary are single letters and the
corresponding values are integers, e.g., {'b': 5, 'a': 6, 'c': 3}. For
each key:value pair in the dictionary the function prints a series of
stars followed by a space, followed by the key. The number of stars
printed is given by the value corresponding to the key. The keys are
printed in alphabetical order.  Note that the key is not printed if the
corresponding value is a number less than 1.

For example, the following code:

print("1.")
draw_histogram({'a': 2, 'c': 7, 'b': 5})
print()

print("2.")
draw_histogram({'a': 0, 'c': 5, 'b': 7, 'f': -1})

prints:

1.
** a
***** b
******* c

2.
******* b
***** c
"""
def draw_histogram(histogram_dict):
    a_dict = {}
    for key in histogram_dict:
        if histogram_dict[key] > 0:
            a_dict[key] = histogram_dict[key]
    items_list = list(a_dict.items())
    items_list.sort()
    my_tuple = tuple(items_list)
    for (character, num) in my_tuple:
        print("*" * num, character)
    pass

def test_draw_histogram():
    print("1.")
    draw_histogram({'a': 2, 'c': 7, 'b': 5})

    print("\n2.")
    draw_histogram({'a': 0, 'c': 5, 'b': 7, 'f': -1})
#--------------------------------------------------
# A helper function
#--------------------------------------------------
def print_dict_in_key_order(a_dict):
    all_keys = list(a_dict.keys())
    all_keys.sort()
    for key in all_keys:
        print(key, ":", a_dict[key])
#--------------------------------------------------
#Print header lines
#--------------------------------------------------
def print_header(number, text):
    text = str(number) + ". " + text
    print("-" * 30)
    print(str(number) * 30)
    print(text)
    print("-" * 30)

main()
