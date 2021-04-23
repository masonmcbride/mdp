from collections import defaultdict

def ValueIteration(mdp):
    """
    1. initialize
    2. update Values
    3. check for convergence
    4. update policy
    """

    # Q(s,a) <- sum(T(s,a,s')[R(s,a,s') + phi*V(s')])
    def Q(state, action):
        return sum(prob*(reward + mdp.discount*V[new_state]) \
                for new_state, prob, reward in mdp.succProbReward(state, action))

    # 1 initialize values (maybe we could do a prior distribution)
    V = defaultdict(int)
    pi = defaultdict()

    # Iterate steps 2-4 
    while True:

        # update values
        newV = defaultdict(int)
        for state in mdp.states:
            if mdp.is_terminal(state):
                newV[state] = 0.
            else:
                newV[state] = max(Q(state, action) for action in mdp.actions(state))

        # check for convergence
        if max(abs(newV[state] - V[state]) for state in mdp.states) < 1e-10:
            break
        V = newV

        # update policy
        for state in mdp.states:
            if mdp.is_terminal(state):
                pi[state] = None
            else:
                pi[state] = max([action for action in mdp.actions(state)], 
                        key=lambda a: Q(state,a))
    return V, pi

