import gym
from gym import spaces
import numpy as np

from typing import Tuple


class tictactoeEnv(gym.Env):
    """
    Implementation of a TicTacToe Environment based on OpenAI Gym standards
    """

    def __init__(self, small: int, large: int) -> None:

        self.n_actions = 9  # for every space on the field
        self.n_states = 8953  # 3**n**2 (n=3) possible combinations, legal states 8953
        self.action_space = spaces.Discrete(self.n_actions)  # 9 actions
        self.observation_space = spaces.Discrete(self.n_states)
        self.small = small  # set the small environment variable for every step
        self.large = large  # set the large environment reward for winning

    def reset(self) -> np.array:
        """
        reset the board game and state
        """
        self.state = np.zeros((3, 3), dtype=int)
        return self.state.flatten()

    def step(self, action: int, color: int) -> Tuple[np.array, int, bool, dict]:
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

        assert self.action_space.contains(action)
        reward = self.small  # give (negative) reward for every move done
        # postion the token on the field
        (row, col) = self.decode_action(action)
        self.state[row, col] = color
        done = self.is_winner(color)
        return self.state, reward, done, {}

    def is_winner(self, color: int) -> bool:
        """check if there is a winner

        Args:
            color (int): of the player

        Returns:
            bool: indicating if there is a winner
        """
        done = False
        boolean_matrix = self.state == color
        for ii in range(3):
            # check if three equal coins are aligned (horizontal, verical or diagonal)
            if (
                np.sum(boolean_matrix[:, ii]) == 3
                or np.sum(boolean_matrix[ii, :]) == 3
                or np.sum(
                    [boolean_matrix[0, 0], boolean_matrix[1, 1], boolean_matrix[2, 2]]
                )
                == 3
                or np.sum(
                    [boolean_matrix[0, 2], boolean_matrix[1, 1], boolean_matrix[2, 0]]
                )
                == 3
            ):
                reward += self.large
                done = True
                break
        return done

    def decode_action(self, i: int) -> list:
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

    def __str__(self) -> None:
        """
        render the board with '-' no stone,
        for stones with 'O' for player = 0, and 'X' for player = 1

        TODO: make an example
        """
        render_field = np.zeros((3, 3), dtype=str)
        for ii in range(3):
            for jj in range(3):
                if self.state[ii, jj] == 0:
                    render_field[ii, jj] = "-"
                elif self.state[ii, jj] == 1:
                    render_field[ii, jj] = "X"
                elif self.state[ii, jj] == 2:
                    render_field[ii, jj] = "O"
        print(render_field)
