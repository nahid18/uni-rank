# Uni-rank

[![Build Status](https://www.travis-ci.com/nahid18/uni-rank.svg?branch=main)](https://www.travis-ci.com/nahid18/uni-rank)

Uni-rank is a mini python package to get the ordered list of USA universities based on their latest ranking on [usnews.com/best-colleges](https://usnews.com/best-colleges)

This package also provides few other information like state, city, zip code and the result can be stored as a `csv` or `json` file.

Installation
----

Uni-rank requires Python 3 to run. 

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
print(usa)


### Helper Functions ###

# 1. Print University Names
rank.print_names()

# 2. Select Universities by States
# Input: State List, Output: DataFrame of filtered universities
states = ['NJ', 'MA']
state_result = rank.select_by_state(states)

# 3. Select Universities by Cities
# Input: City List, Output: DataFrame of filtered universities
cities = ['Cambridge']
city_result = rank.select_by_city(cities)

# You can also get the ordered list by the properties
names = [uni["displayName"] for uni in usa]
print(names)


### Export ###

# Export as CSV
rank.save_csv(usa, "usa_list.csv")

# Export as json
rank.save_json(usa, "usa_list.json")
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
