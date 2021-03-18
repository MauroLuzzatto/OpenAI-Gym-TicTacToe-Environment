from gym.envs.registration import register

register(
    id="TTT-v0",
    entry_point="gym_TicTacToe.envs:tictactoeEnv",
    kwargs={'small': -1, 'large' : 10},
)
