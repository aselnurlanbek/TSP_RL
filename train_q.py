import sys

sys.path.append("../")

from delivery import *
from environment import DeliveryEnvironment

env = DeliveryEnvironment(n_stops=500, method="distance")
agent = DeliveryQAgent(env.observation_space, env.action_space)

run_n_episodes(env, agent, "training_500_stops.gif")
