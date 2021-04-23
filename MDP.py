### Markov Decision Process (where transition probabilities and rewards are given)
### MODEL (MDP problem)
### This is an iterface of an MDP that can 
### interact with my ValueIteration file

class MDP(object):

    def __init__(self, discount=1.0):
        self.discount = discount

    def is_terminal(self, state):
        pass

    def actions(self, state):
        # returns an iterable of all possible actions
        # that can be taken from a given state
        pass

    def succProbReward(self, state, action):
        # return list of (newState, prob, reward) triples
        # state = s, action = a, newState = s'
        # Transition Prob: T(s, a, s'), reward = Reward(s, a, s')
        pass

    def reward(self, state=None, action=None, next_state=None):
        # returns the reward received when transitioning from state s to s'
        # as long as you specify what you are putting in,
        # you don't have to put in all params
        pass

    @property
    def states(self):
        # returns an iterable of all possible states 
        pass

