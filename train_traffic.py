import sys
sys.path.append("../")

from delivery import *
from environment import DeliveryEnvironment

env = DeliveryEnvironment(n_stops=100, method="traffic_box", box_size=0.6, traffic_intensity=100)
agent = DeliveryQAgent(env.observation_space, env.action_space)

run_n_episodes(env, agent, "training_100_stops_traffic.gif")