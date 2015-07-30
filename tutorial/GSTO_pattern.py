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
	'M1': {'8': 1.0},
	'M2': {'4': 1.0},
	'M3': {'10': 1.0},
	'M4': {'12': 1.0},
	'M5': {'14': 1.0},
	}

# The transition probabilities leaving each state.
transitionProbabilities = {
	'R':{'R':0.9, 'M1':0.05, 'D1':0.05},
	'M1':{'I1':0.3, 'M2':0.6, 'D2':0.1},
	'I1':{'I1':0.4, 'M2':0.5, 'D2':0.1},
	'D1':{'M2':0.9, 'D2':0.1},
	'M2':{'I2':0.3, 'M3':0.6, 'D3':0.1},
	'I2':{'I2':0.4, 'M3':0.5, 'D3':0.1},
	'D2':{'M3':0.9, 'D3':0.1},
	'M3':{'I3':0.3, 'M4':0.6, 'D4':0.1},
	'I3':{'I3':0.4, 'M4':0.5, 'D4':0.1},
	'D3':{'M4':0.9, 'D4':0.1},
	'M4':{'I4':0.3, 'M5':0.6, 'D5':0.1},
	'I4':{'I4':0.4, 'M5':0.5, 'D5':0.1},
	'D4':{'M5':0.9, 'D5':0.1},
	'M5':{'R':0.9, 'M1':0.1, 'D1':0.0},
	'D5':{'R':1.0, 'M1':0.0, 'D1':0.0},
	}

model = Hmm(matchEmissions, transitionProbabilities)
