![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)


<img align="right" src="/images/thin-1399_playing_tic_tac_toe_game-512.png" alt="TicTacToe Environment" width="240"/>

# OpenAI Gym – TicTacToe Environment



This repository contains a TicTacToe-Environment based on the OpenAI Gym module and a Q-Learning algorithm that learns to play TicTacToe through self-play.


TicTacToe is a board game, where two players compete to place three stones of their color in parallel (horizontally or vertically) or diagonally to win the game.


## Getting Started
### 1) Setup
```
git clone git@github.com:MauroLuzzatto/OpenAI-Gym-TicTacToe-Environment.git
cd OpenAI-Gym-TicTacToe-Environment
pip install -r requirements.txt
```

### 2) Register the Environment

from the command line
``` 
cd gym-TicTacToe
pip install -e . 
```

the run should end with the following message
```
"Successfully installed gym-TicTacToe"
```
 [Further information on how to register an gym environment](gym-TicTacToe/README.md)


<!-- #### 2.2) Import the Environment
Copy `tictactoe_env.py` from the folder `gymTicTacToe\gym_TicTacToe\envs` to the `TicTacToe` folder

add to the main file:
```python
from tictactoe_env import tictactoeEnv
env = tictactoeEnv()
``` -->

### 3) Run the code
Train the Q-Learning agent to play TicTacToe
```
cd example
```
run `mainTicTacToe.py`


<!-- # Repository Overview
- **gym-TicTacToe**: folder containing the TicTacToe environment and the setup to register the environment
- **QAgent.py**: Implementation of a Q-Learning Algorithm
- **mainTicTacToe.py**: Training loop for the agent to learn to play TicTacToe through self-play
- **utils.py**: helper function to encode the game state, to save and load the Q-table and test the trained agent

--- -->

## TicTacToe Environment


<!---
![TicTacToe Environment](/thin-1399_playing_tic_tac_toe_game-512.png)
-->

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


# Q-Learning Algorithm
The image below describes the Q-Learning Algorithm, which is an oﬀ-policy Temporal-Difference control algorithm:

<!---
![Q-Learning](/Sutton_Barto.png)
-->
<img src="/images/Sutton_Barto.png" alt="TicTacToe Environment" width="600"/>

[Source](http://incompleteideas.net/book/the-book-2nd.html): **Image taken from Richard S. Sutton and Andrew G. Barto, Reinforcement Learning: An Introduction, Second edition, 2014/2015, page 158**

## Legend
- Q: action-value function
- s: state
- s': next state
- a: action
- r: reward
- alpha: learning rate
- gamma: discount factor

## Learning Parameters
- learning_rate = 1.0  
- gamma = 0.9

## Exploration-Exploitation Parameters
- epsilon = 1.
- max_epsilon = 1.
- min_epsilon = 0.0
- decay_rate = 0.000001
 

# References
- [OpenAI Gym](https://gym.openai.com/): Gym is a toolkit for developing and comparing reinforcement learning algorithms from OpenAI
- [Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe)


