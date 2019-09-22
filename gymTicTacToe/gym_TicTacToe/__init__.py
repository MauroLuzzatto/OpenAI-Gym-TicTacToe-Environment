from gym.envs.registration import register

register(
    id='TTT-v4',
    entry_point='gym_TicTacToe.envs:tictactoeEnv',
)
