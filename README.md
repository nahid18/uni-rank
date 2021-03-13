# Uni-rank

Uni-rank provides you the latest ordered list of university rankings around the world. 

Installation
----

Uni-rank requires Python3 to run. 

Install the package by running:
```sh
pip install uni-rank
```

Usage
----
```sh
# import
from unirank import Ranking

# instantiate
rank = Ranking()

# get the ordered list of USA universities
usa = rank.get_usa()

# print the result
print(usa)

# or, save the result as json
rank.save(usa, "usa_list.json")
```

USA University Properties:
----
key | detail
--- | ---
`displayName` | Name
``rankingDisplayRank`` | Rank
`state` | State
`city` | City
`zip` | Zip Code
`description` | Description

License
----

GNU General Public License