# OpenAI Gym: Graph Environment

Adding a new gym environment, based on the following link:

https://github.com/openai/gym/tree/master/gym/envs#how-to-create-new-environments-for-gym

---

## Installation

create the following folder structure (on the same level as the `site-packages\gym` folder in the folder `site-packages`):

* gym-graph/
   * README.md
   * setup.py
   * gym_graph/
      * __init__.py
      * envs/
        * __init__.py
        * graph_env.py

with the following files:

- `gym-graph/setup.py` should have:


```python
from setuptools import setup

  setup(name='gym_graph',
        version='0.0.1',
        install_requires=['gym']  # And any other dependencies foo needs
  )  
```

- `gym-graph/gym_graph/__init__.py` should have:

```python
  from gym.envs.registration import register

  register(
      id='graph-v0',
      entry_point='gym_graph.envs:GraphEnv',
    )
```

- `gym-graph/gym_graph/envs/__init__.py` should have:
```python
from gym_graph.envs.graph_env import GraphEnv
```

- `gym-graph/gym_graph/envs/graph_env.py` should look something like:
```python
  import gym
  from gym import error, spaces, utils
  from gym.utils import seeding

  class GraphEnv(gym.Env):
    ....
```
---

finalize the installation with the following steps:
- download the repo: `git clone git@github.ibm.com:Mauro-Luzzatto/gym-graph.git`
- navigate to `gym-graph` folder with the cmd line: `cd gym-graph`
- use in the cmd line: `pip install -e .`
- in the main gym file, where the environment is used add: `import gym_graph`
- load the environment with `env = gym.make('graph-v0')`

---

# Environments in this repository

1) the TicTacToe environment


