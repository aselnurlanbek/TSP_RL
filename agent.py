import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import random
import time
import random
import numpy as np

from base_agent import Agent


class QAgent(Agent):
    def __init__(self, states_size, actions_size, epsilon=1.0, epsilon_min=0.01, epsilon_decay=0.995, gamma=0.95, lr=0.8):
        self.states_size = states_size
        self.actions_size = actions_size
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.gamma = gamma
        self.lr = lr
        self.Q = self.build_model(states_size,actions_size)

    def build_model(self, states_size, actions_size):
        Q = np.zeros([states_size, actions_size])
        return Q

    def train(self, s, a, r, s_next):
        self.Q[s,a] = self.Q[s,a] + self.rl * (r + self.gamma * np.max(self.Q[s_next,a]) - self.Q[s,a])

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def act(self, s):
        q = self.Q[s,:]

        if np.random.rand() > self.epsilon:
            a = np.argmax(q)
        else:
            a = np.random.randint(self.actions_size)

        return a