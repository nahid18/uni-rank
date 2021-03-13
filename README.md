# Uni-rank

Uni-rank is a mini python package to get the ordered list of USA universities based on their latest ranking on usanews.com

This package also provides few other information like state, city, zip code and the result can be stored as a json file.

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