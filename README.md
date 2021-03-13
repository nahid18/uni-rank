# Uni-rank

Uni-rank provides you the latest list of university rankings around the world.

Installation
----

Uni-rank requires Python3 to run. Install the package by running:
```sh
pip install uni-rank
```

Get the latest USA university rankings:
```sh
from unirank import Ranking

rank = Ranking()
usa = rank.get_usa()

print(usa)
```

License
----

GNU General Public License