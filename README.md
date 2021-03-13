# Uni-rank

Uni-rank provides you the latest list of university rankings around the world.

Installation
----

Uni-rank requires Python3 to run. 

Install the package by running:
```sh
pip install uni-rank
```

Usage:
```sh
# import
from unirank import Ranking

# instantiate
rank = Ranking()

# get the latest ranking of the USA universities
usa = rank.get_usa()

# print the result
print(usa)

# or, save the result as json
rank.save(usa, "usa_list.json")
```


License
----

GNU General Public License