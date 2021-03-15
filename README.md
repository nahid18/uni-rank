# Uni-rank

[![Build Status](https://www.travis-ci.com/nahid18/uni-rank.svg?branch=main)](https://www.travis-ci.com/nahid18/uni-rank)

Uni-rank is a mini python package to get the ordered list of USA universities based on their latest ranking on [usnews.com/best-colleges](https://usnews.com/best-colleges)

This package also provides few other information like `state`, `city`, `zip code`.

The result can be stored as a `csv` or `json` file.

Installation
----

Uni-rank requires Python 3 to run. 

Install the package by running:
```sh
pip install -U uni-rank
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

#print the result
print(usa)
```

Helper Functions
----

**1. Get University Names**
```sh
rank.get_uni_names()
```

**2. Get Top 100 university Names**
```sh
rank.select_top_names(100)
```

**2. Filter Universities by States**

`Input`: State List, 
`Output`: DataFrame of filtered universities

```sh
states = ['NJ', 'MA']
state_result = rank.select_by_state(states)
```

**3. Filter Universities by Cities**

`Input`: City List, 
`Output`: DataFrame of filtered universities

```sh
cities = ['Cambridge']
city_result = rank.select_by_city(cities)
```

Export
----

**1. Export as CSV**
```sh
rank.save_csv(usa, "usa_list.csv")
```

**2. Export as json**
```sh
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
