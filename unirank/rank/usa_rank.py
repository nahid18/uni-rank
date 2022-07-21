from glob import glob
import pandas as pd
import requests
import pkgutil
import random
import json
import os

class Ranking:
    def __init__(self):
        self.api = "https://www.usnews.com/best-colleges/api/search?_sort=rank&_sortDirection=asc&schoolType=national-universities"
        self.header = self._useragent()
        self.dirname = "result"


    def _useragent(self):
        agents = pkgutil.get_data(__package__, "useragents.txt").decode("utf-8")
        return {"User-Agent": random.choice(agents.splitlines())}

    def __read_json(self, filepath):
        with open(filepath, 'r') as fp:
            return json.load(fp)


    def __download_pages(self, pages):
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)
        fetched = []
        done = False
        if pages != []:
            while pages != fetched:
                uncommon = set(pages).difference(set(fetched))
                for page in list(uncommon):
                    url = self.api+"&_page="+str(page)
                    try:
                        raw = requests.get(url=url, headers=self.header, timeout=3)
                        if raw.status_code == 200:
                            data = raw.json()["data"]
                            out_file = f"{self.dirname}/{str(page)}.json"
                            print(f"Saving page {str(page)} to {out_file}")
                            with open(out_file, 'w') as f:
                                json.dump(data, f)
                            fetched.append(page)
                    except:
                        raise Warning(f"Could not fetch {str(page)}")


    def __parse_json(self):
        complete_list = list()
        numbers = sorted([int(i.split('/')[1].split('.')[0]) for i in glob(f"{self.dirname}/*.json")])
        for num in numbers:
            data = self.__read_json(filepath=f"{self.dirname}/{str(num)}.json")
            for item in data["items"]:
                out = dict()
                detail = item["institution"]
                item_keys = ["displayName", "rankingDisplayRank", "state", "city", "zip"]
                for key in item_keys:
                    out[key] = detail[key]
                complete_list.append(out)
        return complete_list


    def get_usa(self):
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)
        total_pages = 0
        while total_pages == 0:
            try:
                raw = requests.get(url=self.api, headers=self.header, timeout=3)
                if raw.status_code == 200:
                    data = raw.json()["data"]
                    total_pages = data["total_pages"]
            except:
                raise Exception("Failed to fetch data")

        downloaded = [int(f.split('/')[-1].split('.')[0]) for f in glob(f"{self.dirname}/*json")]
        remaining = list(set([i for i in range(1,total_pages+1)]) ^ set(downloaded))
        self.__download_pages(pages=remaining)

        data = self.__parse_json()
        return data


    def get_names(self):
        usa = self.get_usa()
        names = [uni["displayName"] for uni in usa]
        return names


    def get_top_names(self, num):
        names = self.get_names()
        return names[:num]


    def select_by_state(self, state_list):
        df = pd.DataFrame(self.get_usa())
        sub = df[df["state"].isin(state_list)]
        return sub


    def select_by_city(self, city_list):
        df = pd.DataFrame(self.get_usa())
        sub = df[df["city"].isin(city_list)]
        return sub


    def save_json(self, inplist, filename):
        if inplist != []:
            with open(filename, 'w') as fh:
                fh.write(json.dumps(inplist, indent=4))


    def save_csv(self, inplist, filename):
        if inplist != []:
            df = pd.DataFrame(inplist)
            df.to_csv(filename, index=False)