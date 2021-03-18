# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 10:05:20 2019

@author: MauroLuzzatto
"""

import numpy as np
import random


class Qagent(object):
    """
    Implementation of a Q-learning Algorithm
    """

    def __init__(
        self, env, state_size, action_size, learning_parameters, exploration_parameters
    ):
        """
        initialize the q-learning agent
        Args:
          state_size (int): ..
          action_size (int): ..
          learning_parameters (dict):
          exploration_parameters (dict):

        """
        # init the Q-table
        self.qtable = np.zeros((state_size, action_size))

        # learning parameters
        self.learning_rate = learning_parameters["learning_rate"]
        self.gamma = learning_parameters["gamma"]

        # exploration parameters
        self.epsilon = exploration_parameters["epsilon"]
        self.max_epsilon = exploration_parameters["max_epsilon"]
        self.min_epsilon = exploration_parameters["min_epsilon"]
        self.decay_rate = exploration_parameters["decay_rate"]

        self.env = env

    def update_qtable(self, state, new_state, action, reward, done):
        """
        update the q-table: Q(s,a) = Q(s,a) + lr  * [R(s,a) + gamma * max Q(s',a') - Q (s,a)]
        Args:
          state (int): current state of the environment
          new_state (int): new state of the environment
          action (int): current action taken by agent
          reward (int): current reward received from env
          done (boolean): variable indicating if env is done
        Returns:
          qtable (array): the qtable containing a value for every state (y-axis) and action (x-axis)
        """
        return self.qtable[state, action] + self.learning_rate * (
            reward
            + self.gamma * np.max(self.qtable[new_state, :]) * (1 - done)
            - self.qtable[state, action]
        )

    def update_epsilon(self, episode):
        """
        reduce epsilon, exponential decay
        Args:
          episode (int): number of episode
        """
        self.epsilon = self.min_epsilon + (
            self.max_epsilon - self.min_epsilon
        ) * np.exp(-self.decay_rate * episode)

    def get_action(self, state, action_space):
        """
        select action e-greedy
        Args:
          state (int): current state of the environment/agent
          action_space (array): array with legal actions
        Returns:
          action (int): action that the agent will take in the next step
        """
        if random.uniform(0, 1) >= self.epsilon:
            # exploitation, max value for given state
            ranks = self.qtable[state, :].argsort().argsort()
            # get ranke of max value (min rank) from the action_space
            action = np.where(ranks == np.min(ranks[action_space]))[0][0]

        else:
            # exploration, random choice
            action = np.random.choice(action_space)  # self.env.action_space.sample()
        return action
