# OpenAI Gym – TicTacToe Enviornment and Training
This repository contains an implementation of a TicTacToe Environment based on OpenAI Gym and a Q-Learning algorithm that learns to play TicTacToe through self-play.

## Getting Started
#### 1) Clone the repo
````
git clone git@github.com:MauroLuzzatto/OpenAI-Gym-TicTacToe-Enviornment.git
````

There are two options to install the gymTicTacToe environment:

#### 2.1) Register the Environment
-	copy the folder `gymTicTacToe` to `C:\Users\[name]\Anaconda3\Lib\site-packages\`

open the command line:
``` 
cd C:\Users\[name]\Anaconda3\Lib\site-packages\gymTicTacToe
pip install -e . 
```

The message appearing should end with *"Successfully installed gym-TicTacToe"*

 [Link to further information on how to register an gym environment](gymTicTacToe/README.md)


#### 2.2) Import the Environment
Copy `tictactoe_env.py` from the folder `gymTicTacToe\gym_TicTacToe\envs` to the `TicTacToe` folder

add to the main file:
```python
from tictactoe_env import tictactoeEnv
env = tictactoeEnv()
```

#### 3) Run

Run `mainTicTacToe.py`

---

## Repository Overview
- **\gymTicTacToe**: folder containing the TicTacToe environment and the setup to register the environment
- **QAgent.py**: Implementation of a Q-Learning Algorithm
- **mainTicTacToe.py**: Training loop for the agent to learn to play TicTacToe through self-play
- **helperFunctions.py**: helper function to encode the game state, to save and load the Q-table and test the trained agent

---

## The TicTacToe Environment
<img align="right" src="/thin-1399_playing_tic_tac_toe_game-512.png" alt="TicTacToe Environment" width="300"/>


TicTacToe is a board game, where two players compete to place three stones of their color in parallel (horizontally or vertically) or diagonally to win the game.

<!---
![TicTacToe Environment](/thin-1399_playing_tic_tac_toe_game-512.png)
-->

### TicTacToe Environment Methods

The environment contains these four main methods:

- reset: reset the board game
- step: add a stone of a color of a player in the board
- decode_action: convert action from 0 to 9 into column and row values
- render: render the stones on the board game


### Reinforcement Learning Environment Properties

#### Actions
The action space contains integers from 0 to 9, each representing a board field. The table below shows the action number and its corresponding board position.


|  |  |  |
| :---: |  :---:  |  :---: |
| 0  | 1  | 2  |
| 3  | 4  | 5  |
| 6  | 7  | 8  |


#### States
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

#### Rewards
There are three different types of rewards in this environment:
-    Large reward (env.large = 10) when the player wins (= +10)
-    Small negative reward (env.small = -1) for every move played (= -1)

#### Done
The game finishes:
-    When one of the players has three stones either horizontally, vertically or diagonally
-    When the board is full of stones, but there is no winner

---

## Q-Learning Algorithm
The image below describes the Q-Learning Algorithm, which is an oﬀ-policy Temporal-Difference control algorithm:

<!---
![Q-Learning](/Sutton_Barto.png)
-->
<img src="/Sutton_Barto.png" alt="TicTacToe Environment" width="750"/>
[Source](http://incompleteideas.net/book/the-book-2nd.html), image taken from **Richard S. Sutton and Andrew G. Barto, Reinforcement Learning: An Introduction, Second edition, 2014/2015, page 158**

#### Variable Explanation
- Q: action-value function
- s: state
- s': next state
- a: action
- r: reward
- alpha: learning rate
- gamma: discount factor

#### Learning Parameters
- learning_rate = 1.0  
- gamma = 0.9

#### Exploration-Exploitation Parameters
- epsilon = 1.
- max_epsilon = 1.
- min_epsilon = 0.0
- decay_rate = 0.000001
 

---

## Main Training Loop
In the training loop the agent learns to play TicTacToe through self-play. After each step taken the Q-table of the agent is updated based on the received reward.

#### Training Settings
- episodes: number of games played by the players
- max_steps: number of maximal steps per game


#### Training Helper Functions
- create_state_dictionary: create state encoding dictionary
- reshape_state: reshape the state array into a tuple
- create_plot: plot the training progress reward versus episodes for both player
- save_qtable: save the Q-table
- load_qtable: load the Q-table
- test_self_play_learning: test the trained agent with playing against it


## References
- [OpenAI Gym](https://gym.openai.com/): Gym is a toolkit for developing and comparing reinforcement learning algorithms from OpenAI
- [Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe)


