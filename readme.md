# Army game

## Summary

Game about civilizations that have multiple armies, at the same time these armies can have branches, that can
be trained to earn points or transformed to be upgraded into another branch in order to earn points. Either a transformation or a training can be done by using the coins. Each army starts with 1000 coins.
One army can attack another, the one that has more points wins 100 coins, on the other part, the loser, losts 2 army branches with the highest score. In case of a tie, both armies lost a branch with the highest score.

## Considerations

There are some decisions made that were not strictly specified on the problem statement:

- Since there is no UI to play the game, there is a script to simulate games randomly.
- One army can attack another army only if they have at least 2 army branches.
- In case of a tie, both armies lost their branch with the highest score.
- Since armies from the same civilization can fight, each army has its own budget(coins).

## How it works

The repo has an script `python game.py` that randomly takes 2 armies, after running a couple or trainings and transformations, they fight. All results are printed on the console. To run the script, please, read the next section.

## Steps to run the game

### Using docker(recommended)

1. On the root project: `docker build . -t army_game`
2. To run the app, `docker run army_game python game.py`
3. To run the tests, `docker run army_game pytest`
4. To run the coverage report, `docker run army_game coverage report`

### Using a virtual environment

1. Install pip https://pip.pypa.io/en/stable/installing/
2. `pip install virtualenv`
3. `python3 -m venv env`
4. `source env/bin/activate`
5. On the root project: `pip install -r requirements.txt`
6. To run the app: `python game.py`
7. To run the tests: `pytest`
8. To run the coverage report: `coverage report`

### Running the project locally

1. Install pip https://pip.pypa.io/en/stable/installing/
2. Install python3 https://docs.python-guide.org/starting/install3/osx/
3. On the root project: `pip install -r requirements.txt`
4. To run the app: `python game.py`
5. To run the tests: `pytest`
6. To run the coverage report: `coverage report`
