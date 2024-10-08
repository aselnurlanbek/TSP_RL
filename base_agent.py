import numpy as np


class Agent(object):
    def __init__(self):
        pass

    def expand_state_vector(self, state):
        if len(state.shape) == 1 or len(state.shape) == 3:
            return np.expand_dims(state, axis=0)
        else:
            return state

    def remember(self, *args):
        self.memory.save(args)