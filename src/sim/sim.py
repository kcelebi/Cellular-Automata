import numpy as np

import sys
sys.path.append('../')

import sim.automata as atm
from sim.rules import Rules
import analysis.analysis as ans
import analysis.stats as stats

'''
	Play through multiple states. Can apply custom rule set and verbosity function.
'''
def play(state, steps, rule = Rules.CONWAY, verbose = False, verbose_func = ans.display_state):
	state = atm.state_fix(state)

	i = 1
	states = np.zeros((steps, *state.shape), dtype = int)
	states[0, :, :] = state
	while i < steps and not stats.is_terminal_state(state):
		if verbose:
			verbose_func(state)
		
		state = atm.update(state, rule = rule)
		states[i, :, :] = state
		i += 1
	
	return states
