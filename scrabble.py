#!/usr/bin/python3

#############################
## Scrabble Anagram Solver ##
#############################

# A program to calculate all possible words made from a collection of letters.
# 
# John W Rogers 2017

from itertools import permutations, combinations, chain
import string, numpy, pdb

# open dictionary and form the dictionary list
with open("./dictionary.sorted") as f:
	dict_list = f.read().splitlines()

# Function to calculate all possible tile permutations
def perm(tiles):
	perm_list=[]
	length = len(tiles)+1

	for i in range(2,length):
		perm_list.append(list(permutations(tiles,i)))
	return perm_list

# Function to calculate all possible words from a list of letters
def scrabble(rack):

	# List of all possible words
	possible = []
	
	# Permutation List
	p_list = []
	
	# create list of permutations
	tmp = list(chain.from_iterable(perm(rack)))
	for p in tmp:
		p_list.append(''.join(p))
	
	# for each permutation check against list of words
	for elem in p_list:
		# Check if word is in the list of words and not already in the list of all possible words
		if (elem in dict_list) and (elem not in possible):
			possible.append(elem)		

	return possible

# Function to calculate the base score based on the letters only
def base_score(word):
	# To be completed
	return 0

# Function to calculate list of possible words when the input letters contain blanks
def blanks(rack):
	# Create list of all letters in the alphabet
	alphabet = list(string.ascii_lowercase)
	w_list = []

	# Calculate all combinations of 2 letter pairs from the alphabet
	c_list = list(combinations(alphabet, 2))
	
	# Generator
	def replaceVals(x):
		for i in range(0,len(x)):
       			yield x[i]

	if rack.count('_') == 1:
		print('One Blank')
		# One Blank
		for letter in alphabet:
			rack.replace('_', letter)
			w_list.append(scrabble(rack))
	elif rack.count('_') == 2:
		# Two Blanks
		#pdb.set_trace()
		print('Two Blanks')
		# Loop through c_list
		for pair in c_list:
			# create generator
			val = replaceVals(pair)
			lstr = numpy.array(list(rack))
			for j in list([i for i in range(len(rack)) if rack[i] =='_']):
			        lstr[j] = next(val)
			w_list.append(scrabble(lstr))	
	else:
		# Error	
		return 0
#	pdb.set_trace()
	r_list = []
	for elem in list(chain.from_iterable(w_list)):
		if elem not in r_list:
			r_list.append(elem)

	return r_list
print(blanks('a_b_c'))
