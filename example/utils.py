# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:50:10 2019

@author: mauro
"""

import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from collections import Counter


def create_state_dictionary():
    """
    create a dictionary, that encodes the game postions (3x3) into a state number (int)
    Returns:
      state_dict (dict): key = game position, value = state number
    """
    state_number = 0
    state_dict = {}

    # create all digit combinations with 0,1,3 for 9 digit number
    for game_position in set(product(set(range(3)), repeat=9)):
        # count the digits per tuple
        count_digits = Counter(game_position)
        # remove all board situation, which are not possible
        if abs(count_digits[1] - count_digits[2]) <= 1:
            state_dict[game_position] = state_number
            state_number += 1
    print("Number of legal states: {}".format(state_number))
    return state_dict


def reshape_state(state):
    """
    transfrom the 3x3 board numpy array into a flattend tuple
    Args:
        state (array): 3x3 numpy array, representing the board postions = state
    Returns:
        state (tuple): the flattened numy array converted into a tuple
    """
    return tuple(state.reshape(1, -1)[0])


def create_plot(player1_reward_array, player2_reward_array):
    """
    plot the rewards of the player 1 and 2 versus the number of training episode in self-play
    Args:
        player1_reward_array (array): rewards over training episoded player1
        player2_reward_array (array): rewards over training episoded player2
    """
    plt.figure(figsize=(10, 5))
    plt.title("reward over time")
    plt.plot(
        range(len(player1_reward_array)), player1_reward_array, label="Reward Player 1"
    )
    plt.plot(
        range(len(player2_reward_array)), player2_reward_array, label="Reward Player 2"
    )
    plt.legend()
    plt.grid()
    plt.show()


def save_qtable(qtable, name="qtable"):
    """
    save the qtable
    """
    np.save("{}.npy".format(name), qtable)
    print("{}.npy saved!".format(name))


def load_qtable(name="qtable"):
    """
    load the qtable
    """
    return np.load("{}.npy".format(name))


def test_self_play_learning(env, qtable, max_steps, num_test_games, state_dict):
    """
    play against the trained Q-Learning agent
    Args:
        env (class): environment class
        qtable (array): numpy array containing the qtable respect. the state-action values
        max_steps (int): max steps to take in one episode
        num_test_games (int): number of times to play against the trained agent
        state_dict (dict): encoding of the state array
    """

    player1 = 1
    player2 = 2

    for _ in range(num_test_games):
        state = env.reset()
        state = state_dict[reshape_state(state)]

        action_space = np.arange(9)
        start = np.random.randint(2)  # 0 or 1

        if start == 0:
            print("Player 1 beginns (Human)")
        else:
            print("Player 2 beginns (QAgent)")
        print("--" * 10)
        print("--" * 10)

        for _step in range(start, max_steps + start):

            # alternate the moves of the players
            if _step % 2 == 0:
                env.render()
                print("--" * 10)
                print("Move Player 1")
                action = np.nan

                while action not in action_space:
                    action = int(
                        input("choose an action from {}: ".format(action_space))
                    )
                    print("Action:", action)
                action_space = action_space[action_space != action]

                state, reward, done, _ = env.step(action, player1)
                state = state_dict[reshape_state(state)]
                print(reward)
                if done:
                    print("**" * 10)
                    print("player 1 won!")
                    print("**" * 10)
                    env.render()
                    print("\n" * 2)
                    break
            else:
                print("--" * 10)
                print("move player 2")

                array = np.array(qtable[state, :])
                order = array.argsort()
                ranks = order.argsort()
                max_value_rank = np.min(ranks[action_space])
                action = np.where(ranks == max_value_rank)[0][0]

                print("Action:", action)
                action_space = action_space[action_space != action]

                state, reward, done, _ = env.step(action, player2)
                state = state_dict[reshape_state(state)]
                if done:
                    print("**" * 10)
                    print("player 2 won!")
                    print("**" * 10)
                    env.render()
                    print("\n" * 2)
                    break

            # stopping criterion
            if not done and _step == max_steps + start - 1:
                if reward != env.large - 1:
                    print("There is no Winner!")
                    print("--" * 10)
                    print("--" * 10)
                    print("\n" * 2)
                break
