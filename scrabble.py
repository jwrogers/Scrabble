#!/usr/bin/python3

#############################
## Scrabble Anagram Solver ##
#############################

# A program to calculate all possible words made from a collection of letters.
# 
# John W Rogers 2017

from itertools import permutations, combinations, chain
import string, numpy

# Scoring Dictionary
scores = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10, '_':0}

# open dictionary and form the dictionary list
with open("./dictionary.sorted") as f:
	dict_list = f.read().splitlines()

# Create list of all letters in the alphabet
alphabet = list(string.ascii_lowercase)
	

# Function to calculate all possible tile permutations
def perm(tiles):
	perm_list=[]
	length = len(tiles)+1

	for i in range(2,length):
		perm_list.append(list(permutations(tiles,i)))
	return perm_list

# Function to calculate all possible anagrams of given letters 
def scrabble(rack):
	p_list = []
	length = len(rack)+1	
	for i in range(2,length):
		p_list = []
		# Create list of permutations
		tmp = list(permutations(rack, i))
		for p in tmp:
			p_list.append(''.join(p))
		tmp = []
		
		# check if word is in list of words 
		possible = []
		for elem in p_list:
			if (elem in dict_list) and (elem not in possible):
				possible.append(elem)
		possible.reverse()
		for j in range(len(possible)):
			print(possible.pop())

# Function to calculate the base score based on the letters only
def base_score(word):

	score = 0

	for letter in list(word):
		score += scores[letter]

	return score

# Function to calculate list of possible words when the input letters contain blanks
def blanks(rack):
	
	w_list = []

	# Calculate all combinations of 2 letter pairs from the alphabet
	c_list = list(combinations(alphabet, 2))
	r_list = []
	
	# Generator
	def replaceVals(x):
		for i in range(0,len(x)):
       			yield x[i]
	# One Blank
	if rack.count('_') == 1:
		
		for letter in alphabet:
			w_list.append(scrabble(rack.replace('_',letter)))

		for elem in list(chain.from_iterable(w_list)):
			if elem not in r_list:
				r_list.append(elem)
	# Two Blanks
	elif rack.count('_') == 2:
		
		# Loop through c_list
		for pair in c_list:
			# create generator
			val = replaceVals(pair)
			lstr = numpy.array(list(rack))
			for j in list([i for i in range(len(rack)) if rack[i] =='_']):
			        lstr[j] = next(val)
			w_list.append(scrabble(lstr))	

		for elem in list(chain.from_iterable(w_list)):
			if elem not in r_list:
				r_list.append(elem)
	# No Blanks
	else:
		r_list = scrabble(rack)

	return r_list
# User input
rack = input('Enter the letters: ').lower()
for el in [elem for elem in rack]:
	if (el not in alphabet) and (el != '_') :
		#error
		quit()

