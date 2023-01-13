# Cut and paste this text into a text editor and save in a file 
# christmasgreetings.py
# then execute it as a Python program

# AUTHOR Paul Curzon, QMUL www.cs4fn.org
# This is a christmas card writing program to save all that time writing cards
# This program was inspired by the 'first creative program' written by Chris Strachey,
# It was a love letter writing program
# The program provides a few template sentences to use.
# It uses them in a random order, filling them with words from word lists
# The word lists are for different grammatical categories like nouns and verbs

# Modify this program by adding new words to the word list
# And adding new sentence templates

# Alternatively modify it to be a christmas card love letter
# Or modify it for some other occasion

import random

# Define global constants

# This gives the number of sentences the program can choose from
# Add 1 to this number for each new sentence template you add to the program
NUMBER_OF_TEMPLATES = 3


# Pick a word at random from a given word list removing it so it isn't used again
def ChooseWord(wordlist) :
	word = random.choice(wordlist)
	wordlist.remove(word)
	return word

# Pick a random number from a list of integers removing it so it isn't used again
def PickRandomNumber(ns) :
	n = random.choice(ns)
	ns.remove(n)
	return n

# Sentence Template
# I wish you a ADJECTIVE NOUN.
def IWishYou(adjectives, nouns) :
	noun = ChooseWord(nouns)
	adjective = ChooseWord(adjectives)
	print("I wish you a " + adjective + " " + noun + ".")


# Sentence Template
# I hope VERB you ADVERB.
def IHopeTo(verbs, adverbs) :
	verb = ChooseWord(verbs)
	adverb = ChooseWord(adverbs)
	print("I hope " + verb + " you " + adverb + ".")

# Sentence Template
# Have a ADJECTIVE NOUN.	
def HaveA(adjectives, nouns) :
	adjective = ChooseWord(adjectives)
	noun = ChooseWord(nouns)
	print("Have a " + adjective + " " + noun + ".")

# Sentence Template
# SALUTATION!	
def Salutation(salutations) :
	salutation = ChooseWord(salutations)
	print()
	print(salutation + "!")

# Sentence Template
#  END Q	
def SignOff(endings) :
	end = ChooseWord(endings);
	print(end);
	print("Q");

# Create a christmas greeting using the template sentences and word lists below
# Always start with a salutation and end with a sign off
# In between choose the templates in a random order and substitute in words from 
# the appropriate word lists at random
def GenerateChristmasGreeting() :  
	salutations =  ["Happy Christmas", "Merry Christmas", "Season's Greetings", "Happy New Year"]
	adjectives =   ["wonderful", "joyous", "peaceful", "relaxing", "great"]
	nouns =        ["holiday", "time", "few weeks", "christmas"]
	verbs =        ["to see", "to catch up with", "to be with", "to meet up with"]
	adverbs =      ["soon", "in the new year", "sometime soon", "before long"]
	endings =      ["With love", "Best wishes", "All my love"]
	
	Salutation(salutations)
	
	templatesleft = list(range(0,NUMBER_OF_TEMPLATES))
	
	while len(templatesleft)>0 :
		sentencechoice = PickRandomNumber(templatesleft)
		if (sentencechoice == 0) :
			IWishYou(adjectives, nouns)
		elif (sentencechoice == 1) :
			IHopeTo(verbs, adverbs)
		elif (sentencechoice == 2) :
			HaveA(adjectives, nouns)
		else :
			print("I'm lost for words")
        
	SignOff(endings)

GenerateChristmasGreeting() 