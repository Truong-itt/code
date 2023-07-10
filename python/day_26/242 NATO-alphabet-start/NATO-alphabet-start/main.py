

import pandas

bien_a=pandas.read_csv('nato_phonetic_alphabet.csv')

print(bien_a)
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
c = {row.letter:row.code for (index,row) in bien_a.iterrows()}
print(c)


# bien = [key:value for (key,value)]
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
a = input('Enter a word:').upper()
output_list = [c[i] for i in a]
print(output_list)