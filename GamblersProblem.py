"""
FROM: http://www.incompleteideas.net/sutton/book/first/4/node5.html
A gambler has the opportunity to make bets on the outcomes of a sequence of coin flips.
If the coin comes up heads, then he wins as many dollars as he has staked on that flip,
but if it is tails then he loses his stake. 
The game ends when the gambler wins by reaching his goal of 100 dollars,
or loses by running out of money. On each flip, 
the gambler must decide what portion of his capital to stake, in integer numbers of dollars. 
This problem can be formulated as an undiscounted, episodic, finite MDP.

state: s in {1,2,...,99}
action(state): a in {0,1,...,min(s,100-s)}
reward(state): 1 if state is terminal and 0 otherwise

parameters: 
    p: the probability of the coin landing heads
"""

from MDP import *
from ValueIteration import *

class GamblersProblem(MDP):
    def __init__(self, p):
        super().__init__(discount=1.0, goal=100)
        self.p = p
        self.goal = goal

    def is_terminal(self, state):
        return state == goal or state < 0

    def actions(self, state):
        # returns an iterable of all possible actions
        # that can be taken from a given state
        return range(1, min(s, goal-s)+1)

    def succProbReward(self, state, action):
        # return list of (newState, prob, reward) triples
        # state = s, action = a, newState = s'
        # Transition Prob: T(s, a, s'), reward = Reward(s, a, s')

        # when you are in state s and take action a,
        # There are two cases: you win with prob p or lose with prob 1-p
        heads_state = state + action
        tails_state = state - action
        case1 = (heads_state, self.p, reward(next_state=heads_state))
        case2 = (tails_state, 1-self.p, reward(next_state=losing_state))
        return [case1, case2]

    def reward(self, state=None, action=None, next_state=None):
        # returns the reward received when transitioning from state s to s'
        # as long as you specify what you are putting in,
        # you don't have to put in all params
        return 1 if self.is_terminal(next_state) and next_state == goal else 0

    def states(self):
        # returns an iterable of all possible states
        return range(1, goal)


if __name__ == "__main__":
    gp = GamblersProblem(p=0.44)

    V, pi = ValueIteration(gp)
    print(f"Values: {V}")
    print(f"Policy: {pi}")
