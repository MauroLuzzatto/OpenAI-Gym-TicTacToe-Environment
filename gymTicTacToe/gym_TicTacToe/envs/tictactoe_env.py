import gym
from gym import spaces
import numpy as np


class tictactoeEnv(gym.Env):
    """
    Implementation of a TicTacToe Environment based on OpenAI Gym standards

    """
    def __init__(self):

        self.n_actions = 9 # for every space on the field
        self.n_states = 8953    # 3**n**2 (n=3) possible combinations, legal states 8953
        self.action_space = spaces.Discrete(self.n_actions)     # 9 actions
        self.observation_space = spaces.Discrete(self.n_states)     
        self.small = -1
        self.large = 10  # set the large enviornment reward



    def reset(self):
        """
        reset the board game and state
        """
        self.state = np.zeros((3,3), dtype=int)
        return self.state.flatten()


    def step(self, action, color):
        """
        step function of the tictactoeEnv
        Args:
          action (int): integer between 0-8, each representing a field on the board
          color (int): 1 or 2, representing the color of stones of the players
        Returns:
          self.state (tuple): state of the current board position, 0 means no stone, 1 or 2 are stones placed by the players
          reward (int): reward of the currrent step
          done (boolean): true, if the game is finished
        """

        # check if action is contained in action_sapce
        assert self.action_space.contains(action)

        # initiale values
        done = False
        # give (negative) reward for every move done
        reward = self.small

        # set the token on the field
        (row, col) = self.decode_action(action)
        self.state[row, col] = color

        # check if there is a winner
        boolean_matrix = self.state == color
        for ii in range(3):
            # check if three equal coins are aligned (horizontal, verical or diagonal)
            if np.sum(boolean_matrix[:, ii]) == 3 or \
               np.sum(boolean_matrix[ii, :]) == 3 or \
               np.sum([boolean_matrix[0,0], boolean_matrix[1,1], boolean_matrix[2,2]]) == 3 or \
               np.sum([boolean_matrix[0,2], boolean_matrix[1,1], boolean_matrix[2,0]]) == 3:
                reward += self.large
                done = True
                break

        return self.state, reward, done, {}


    def decode_action(self, i):
        """
        decode the action integer into a colum and row value,
        0 = upper left corner, 8 = lower right corner
        """
        out = []
        out.append(i % 3)
        i = i // 3
        out.append(i)
        assert 0 <= i < 3
        return reversed(out)


    def render(self):
        """
        render the board with '-' no stone,
        for stones with 'O' for player = 0, and 'X' for player = 1
        """
        render_field = np.zeros((3,3), dtype = str)
        for ii in range(3):
            for jj in range(3):
                if self.state[ii,jj] == 0:
                    render_field[ii, jj] = '-'
                elif self.state[ii,jj] == 1:
                    render_field[ii, jj] = 'X'
                elif self.state[ii,jj] == 2:
                    render_field[ii, jj] = 'O'
        print(render_field)
