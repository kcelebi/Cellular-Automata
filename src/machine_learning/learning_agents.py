import sys
sys.path.append('../')

from path_handler import PathHandler as PH
import sim.automata as atm
from sim.rules import Rules


__all__ = ['ReinforcementAgent']

class Agent:

	def __init__(self, index = 0):
		self.index = index

	def get_action(self, state):
		raise NotImplementedError()


class ValueEstimationAgent(Agent):
	
	"""
      Abstract agent which assigns values to (state,action)
      Q-Values for an environment. As well as a value to a
      state and a policy given respectively by,

      V(s) = max_{a in actions} Q(s,a)
      policy(s) = arg_max_{a in actions} Q(s,a)

      Both ValueIterationAgent and QLearningAgent inherit
      from this agent. While a ValueIterationAgent has
      a model of the environment via a MarkovDecisionProcess
      (see mdp.py) that is used to estimate Q-Values before
      ever actually acting, the QLearningAgent estimates
      Q-Values while acting in the environment.
    """

	def __init__(self, alpha, epsilon, gamma, num_training):
		'''
	        alpha    - learning rate
	        epsilon  - exploration rate
	        gamma    - discount factor
	        num_training - number of training episodes, i.e. no learning after these many episodes
        '''
		self.alpha = alpha
		self.epsilon = epsilon
		self.gamma = gamma
		self.num_training = num_training

	def get_Q_value(self, state, action):
		raise NotImplementedError()

	def get_value(self, state):
		raise NotImplementedError()

	def get_policy(self, state):
		raise NotImplementedError()

	def get_action(self, state):
		raise NotImplementedError()

class ReinforcementAgent(ValueEstimationAgent):

	def update(self, state, action, next_state, reward):
		raise NotImplementedError()

	def get_legal_actions(self, state):
		return self.action_func(state)

	def observe_transition(self, state, action, next_state, delta_reward):
		self.episode_rewards += delta_reward
		self.update(state, action, next_state, delta_reward)

	def start_episode(self):
		...

	def stop_episode(self):
		...

	def __init__(self, action_func = None, num_training = 100, epsilon = 0.5, alpha = 0.5, gamma = 1):
		# we should never be in this position, overwrite this later
		if action_func is None:
			action_func = lambda state: state.get_legal_actions() # not possible, state not an obj

		self.action_func = action_func
		self.episodes_so_far = 0
		self.accum_train_rewards = 0.0
		self.accum_train_rewards = 0.0
		self.num_training = int(num_training)
		self.epsilon = float(epsilon)
		self.alpha = float(alpha)
		self.discount = float(gamma)

	





