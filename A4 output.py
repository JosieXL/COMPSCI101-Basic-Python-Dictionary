
------------------------------
111111111111111111111111111111
1. test_draw_histogram()
------------------------------
1.
** a
***** b
******* c

2.
******* b
***** c

------------------------------
222222222222222222222222222222
2. test_get_word_len_dict()
------------------------------
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

------------------------------
333333333333333333333333333333
3. test_get_text_valuation()
------------------------------
1. BLAH - 7
2. thought provoking - 40
3. too much month at the end of the money - 70

------------------------------
444444444444444444444444444444
4. test_remove_short_synonyms()
------------------------------
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

------------------------------
555555555555555555555555555555
5. test_get_triples_dict()
------------------------------
1.
per : 2
upe : 2

2.
abc : 3
bca : 2
cab : 2

3.
est : 2
sma : 2

4.
ain : 3
epa : 2
gin : 2
ing : 3
int : 4
myd : 2
ngi : 3
nti : 3
pai : 3
tin : 3

------------------------------
666666666666666666666666666666
6. test_contains_keys_and_values()
------------------------------
1. True
2. True
3. False
4. False
5. False

------------------------------
777777777777777777777777777777
7. test_get_previous_words_dict()
------------------------------
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

