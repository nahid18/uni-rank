# Uni-rank

Uni-rank is a mini python package to get the ordered list of USA universities based on their latest ranking on [usnews.com](https://usnews.com/best-colleges)

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

# get the ordered list of university names
names = [uni["displayName"] for uni in usa]
print(names)

# Optional: you can save the result as json
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


Note
----
Intend to extend the package to support other types of rankings and also include other countries on later versions, hence the name `uni-rank` not `usa-rank`

License
----

GNU General Public License
