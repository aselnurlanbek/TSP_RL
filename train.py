from environment import DeliveryEnvironment

env = DeliveryEnvironment(n_stops=10)
env.render()

env.stops

for i in [0, 1, 2, 3]:
    env.step(i)

env.render()

