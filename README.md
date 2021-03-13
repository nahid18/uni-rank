# Uni-rank

Uni-rank provides you the latest list of university rankings around the world.

Installation
----

Uni-rank requires Python3 to run. 

Install the package by running:
```sh
pip install uni-rank
```

Import into your code:
```sh
from unirank import Ranking
```

Get the latest USA Universities Ranking:
```sh
rank = Ranking()
usa = rank.get_usa()
print(usa)
```

You can save the result as json:
```sh
rank = Ranking()
usa = rank.get_usa()
save(usa, "usa_list.json")
```


License
----

GNU General Public License