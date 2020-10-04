# Army game

## Summary

Army game: this game is about civilizations that can have multiple armies, at the same time these armies can have branches, that can
be trained and transformed into another branch in order to have more points.
One army can attack another, the one that have more points wins.

## Steps

### Using docker(recommended)

1. On the root project: `docker build . -t army_game`
4. To run the app, `docker run army_game python game.py`
5. To run the tests, `docker run army_game pytest`
6. To run the coverage report, `docker run army_game coverage report`

### Runing the project locally

1. Install pip https://pip.pypa.io/en/stable/installing/
2. Install python3 https://docs.python-guide.org/starting/install3/osx/
3. On the root project: `pip install -r requirements.txt`
4. To run the app: `python game.py`
5. To run the tests: `pytest`
6. To run the coverage report: `coverage report`


