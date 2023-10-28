![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)


<img align="right" src="/images/tictactoe.png" alt="TicTacToe Environment" width="250"/>

# OpenAI Gym – TicTacToe Environment



This repository contains a TicTacToe-Environment based on the OpenAI Gym module.

An example on how to use this environment with a Q-Learning algorithm that learns to play TicTacToe through self-play can be found [here](https://github.com/MauroLuzzatto/learn-tictactoe-through-self-play).

TicTacToe is a board game, where two players compete to place three stones of their color in parallel (horizontally or vertically) or diagonally to win the game.



| Environment Id | Observation Space |Action Space| Reward Range | tStepL | 
| ------ | ------ |------ | ------ |------ | 
| TTT-v0 |Box(3,3)|Discrete(9)|(-inf, inf) | 9 | 



## Getting Started
### 1) Setup
```
git clone git@github.com:MauroLuzzatto/OpenAI-Gym-TicTacToe-Environment.git
cd OpenAI-Gym-TicTacToe-Environment
pip install -r requirements.txt
```

### 2) Register the Environment

run the following command in the command line
``` 
pip install -e gym-TicTacToe/. 
```

now you should see the following message
```
"Successfully installed gym-TicTacToe"
```
Further information on how to register an gym environment can be found  [here](gym-TicTacToe/README.md)



### 3) Use the environment and start playing
```
import gym_TicTacToe
import gym

# initialize the tictactoe environment
env = gym.envs.make("TTT-v0", small=-1, large=10)

# start playing
color = 1
action = 0
new_state, reward, done, _ = env.step((action, color))
```



## TicTacToe Environment


###  Methods

The environment contains the following four main methods:

- **reset**: reset the board game
- **step**: add a stone of a color of a player in the board
- **decode_action**: convert action from 0 to 9 into column and row values
- **render**: render the stones on the board game


### Actions
The action space contains integers from 0 to 9, each representing a board field. The table below shows the action number and its corresponding board position.


|  |  |  |
| :---: |  :---:  |  :---: |
| 0  | 1  | 2  |
| 3  | 4  | 5  |
| 6  | 7  | 8  |


### States
State space:
-    On a 3x3 board are theoretically 3^n^2 = 3^3^2 = 19’683 stone combinations of two different colors (and no color) possible (n = the size of the square filed)
-    However, not all combinations are legal (e.g. you can have a board full of stones from one color)
-    The state space can therefore be reduced to 8’953 states

State representation:
-    The state is represented as a 3x3 numpy array representing the 9 fields of the board
-    Dependent on the moves, the array will get the value
    - 0 for no stone,
    - 1 = stone of player 1
    - 2 = stone of player 2

### Rewards
There are three different types of rewards in this environment:
-    Large reward (env.large = 10) when the player wins (= +10)
-    Small negative reward (env.small = -1) for every move played (= -1)

### Done
The game finishes:
-    When one of the players has three stones either horizontally, vertically or diagonally
-    When the board is full of stones, but there is no winner




## References
- [OpenAI Gym](https://gym.openai.com/): Gym is a toolkit for developing and comparing reinforcement learning algorithms from OpenAI
- [Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe)


