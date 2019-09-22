# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:22:09 2019

@author: MauroLuzzatto


Description:

Implementation of environment and a q-learning algorithm 
that learns to play TicTacToe through self-play 

"""

import numpy as np
import gym
import time

import gym_TicTacToe
from Qagent import Qagent

from helperFunctions import create_state_dictionary, reshape_state, \
                            load_qtable, save_qtable, test_self_play_learning

state_dict = create_state_dictionary()


# init the enviornment
env = gym.make('TTT-v4')


# second option:
#from tictactoe_env import tictactoeEnv
#env = tictactoeEnv()


state_size = env.observation_space.n 
action_size = env.action_space.n

player1 = 1
player2 = 2


learning_parameters = {
   'learning_rate':1.0,  
   'gamma':0.9
   }

exploration_parameters = {
    'epsilon': 1.,
    'max_epsilon': 1.,
    'min_epsilon': 0.0,
    'decay_rate': 0.000001
    }

# set training parameters
episodes = 10**6 * 2
max_steps = 9

# name of the qtable when saved
name = 'qtable'
load = True
save = True
test = True

num_test_games = 3

player1_reward_array = np.zeros(episodes)
player2_reward_array = np.zeros(episodes)

# init the q-learning algorithm
qagent = Qagent(env, state_size, action_size, learning_parameters, exploration_parameters)

if load:
    try:
        qagent.qtable = load_qtable(name)
        print('{}.npy loaded!'.format(name))

    except: 
        print('qtable could not be loaded!')
        


# TODO: Track the actions taken over time while playing,  9*8*7*6*5*4*3*2*1

# start the training
start_time = time.time()

for episode_i in range(episodes):
    state = env.reset()
    state = state_dict[reshape_state(state)]
    
    action_space = np.arange(9)

    # reset the reward of the players
    player1_reward = 0
    player2_reward = 0

    # change start of players, randomly change the order players to start the game
    start = np.random.randint(2) # integer either 0 or 1
        
    for _step in range(start, max_steps + start):
        # alternate the moves of the players
        if _step%2 == 0:
 
            # player 1
            action = qagent.get_action(state, action_space)
            
            # remove action from the action space
            action_space = action_space[action_space != action]
               
            new_state, reward, done, _ = env.step(action, player1)
            new_state = state_dict[reshape_state(new_state)]

            qagent.qtable[state, action] = qagent.update_qtable(state, new_state, action, reward, done)
            # new state
            state = new_state
            player1_reward += reward

        else:            
 
            # player 2
            action = qagent.get_action(state, action_space)
            
            # remove action from the action space
            action_space = action_space[action_space != action]            

            new_state, reward, done, _ = env.step(action, player2)
            new_state = state_dict[reshape_state(new_state)]

            qagent.qtable[state, action] = qagent.update_qtable(state, new_state, action, reward, done)
            
            # new state
            state = new_state
            player2_reward += reward
        
        # stopping criterion
        if done == True:
            break
    
    # reduce epsilon for exporation-exploitation tradeoff
    qagent.update_epsilon(episode_i)
    
    player1_reward_array[episode_i] = player1_reward
    player2_reward_array[episode_i] = player2_reward
    
    if episode_i % 100000 == 0:
        print('episode: {}, epsilon: {}'.format(episode_i, round(qagent.epsilon,2)))
        print('elapsed time [min]: {}, done [%]: {}'.format(round((time.time() - start_time)/60.,2), 
                                                            episode_i/episodes * 100)) 


if save:
    save_qtable(qagent.qtable, name)
    qtable = qagent.qtable
    
# test the algorithm with playing against it
if test:            
    test_self_play_learning(env, qtable, max_steps, num_test_games, state_dict)