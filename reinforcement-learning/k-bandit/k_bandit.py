# from random import randint, random, choice, uniform, seed
import random
import numpy as np
import matplotlib.pyplot as plt


class Env:
    """Avg action value
    """

    def __init__(self, k, epsilon=0.1):
        self.k = k
        self.epsilon = epsilon
        self.avg_rewards = np.zeros(k)

        # Hard code bandits to be gausian distributions.
        self.distribustion_means = np.linspace(0.1, 0.9, num=self.k)

        # Pick a random for each distribution
        self.avg_rewards = np.array(
            [np.random.normal(loc=self.distribustion_means[i])
             for i in range(k)]
        )
        self.step = 0
        self.step_a = np.zeros(self.k)
        self.step_reward = 0

    def next_action(self):
        self.step += 1
        rand = random.random()
        if rand <= self.epsilon:
            # Non greedy action
            choice_k = random.randint(1, self.k)-1
        else:
            # Greedy action
            choice_k = np.argmax(self.avg_rewards)

        self.step_a[choice_k] += 1

        self.step_reward = np.random.normal(self.distribustion_means[choice_k])
        self.avg_rewards[choice_k] = self.avg_rewards[choice_k] + \
            (self.step_reward -
             self.avg_rewards[choice_k])/(self.step_a[choice_k])


def run(k, n_steps, n_runs, eps):
    steps = np.zeros((n_steps+1, n_runs))

    for n_run in range(n_runs):

        env = Env(k, epsilon=eps)
        steps[0, n_run] = env.step_reward

        for step in range(1, n_steps):
            env.next_action()
            steps[step, n_run] = env.step_reward

    return steps


k = 10
n_steps = 2000
n_runs = 5000
eps = [0, 0.1, 0.01]

plt.figure(figsize=(16, 9))
for e in eps:
    color = "#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
    steps = run(k, n_steps, n_runs, e)
    plt.plot(range(n_steps+1), np.mean(steps, axis=1),
             c=color, label=f'Eps: {e}')
plt.legend()
plt.show()
