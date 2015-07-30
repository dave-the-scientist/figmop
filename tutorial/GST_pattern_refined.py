from patternHmm import Hmm

min_matches = 4
max_genome_region = 40000
meme_file = '/home/dave/Desktop/figmop/test/meme_out_20/meme.txt'

# For theoretical reasons, each row in the two dictionaries below should sum to
# 1.0. However there is nothing in the program that relies on this, and so it is
# not strictly necessary. 'M' refers to the match states, 'I' refers to the
# insert states, 'D' refers to the delete states, and 'R' is a general random
# state, indicating sequence between matches.

# Emission probabilities of the Match states. Replace the letters with any string.
matchEmissions = {
	'M1': {'2': 1.0, '15':0.5},
	'M2': {'13': 1.0},
	'M3': {'4': 1.0},
	'M4': {'1': 1.0, '11':0.5, '10':0.5},
	'M5': {'6': 1.0, '19':0.8},
	'M6': {'7': 1.0},
	'M7': {'3': 1.0},
	'M8': {'18': 1.0},
	'M9': {'5': 1.0},
	}

# The transition probabilities leaving each state.
transitionProbabilities = {
	'R':{'R':0.9, 'M1':0.05, 'D1':0.05},
	'M1':{'I1':0.25, 'M2':0.55, 'D2':0.2},
	'I1':{'I1':0.4, 'M2':0.5, 'D2':0.1},
	'D1':{'M2':0.9, 'D2':0.1},
	'M2':{'I2':0.3, 'M3':0.6, 'D3':0.1},
	'I2':{'I2':0.4, 'M3':0.5, 'D3':0.1},
	'D2':{'M3':0.9, 'D3':0.1},
	'M3':{'I3':0.3, 'M4':0.6, 'D4':0.1},
	'I3':{'I3':0.4, 'M4':0.5, 'D4':0.1},
	'D3':{'M4':0.9, 'D4':0.1},
	'M4':{'I4':0.25, 'M5':0.5, 'D5':0.25},
	'I4':{'I4':0.4, 'M5':0.5, 'D5':0.1},
	'D4':{'M5':0.9, 'D5':0.1},
	'M5':{'I5':0.25, 'M6':0.55, 'D6':0.2},
	'I5':{'I5':0.4, 'M6':0.5, 'D6':0.1},
	'D5':{'M6':0.9, 'D6':0.1},
	'M6':{'I6':0.3, 'M7':0.6, 'D7':0.1},
	'I6':{'I6':0.4, 'M7':0.5, 'D7':0.1},
	'D6':{'M7':0.9, 'D7':0.1},
	'M7':{'I7':0.25, 'M8':0.55, 'D8':0.2},
	'I7':{'I7':0.4, 'M8':0.5, 'D8':0.1},
	'D7':{'M8':0.9, 'D8':0.1},
	'M8':{'I8':0.3, 'M9':0.6, 'D9':0.1},
	'I8':{'I8':0.4, 'M9':0.5, 'D9':0.1},
	'D8':{'M9':0.9, 'D9':0.1},
	'M9':{'R':0.9, 'M1':0.1, 'D1':0.0},
	'D9':{'R':1.0, 'M1':0.0, 'D1':0.0},
	}

model = Hmm(matchEmissions, transitionProbabilities)
