import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import time
from tqdm import tqdm_notebook

from delivery import *
from environment import DeliveryEnvironment

env = DeliveryEnvironment(n_stops=10)
env.render()

env.stops

for i in [0, 1, 2, 3]:
    env.step(i)

env.render()

