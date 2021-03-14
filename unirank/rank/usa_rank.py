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


    def __useragent(self):
        agents = pkgutil.get_data(__package__, "useragents.txt").decode("utf-8")
        return random.choice(agents.splitlines())


    def __save_initial(self):
        usnews = header_selected = dict()
        header_selected = dict()
        fetched = False
        while fetched != True:
            try:
                ua = self.__useragent()
                headers = {"User-Agent": ua}
                data = requests.get(url=self.api, headers=headers, timeout=3)
                if data.status_code == 200:
                    header_selected = headers
                    usnews = data.json()
                    with open("apidata/1.json", 'w') as fw:
                        json.dump(usnews, fw)
                    fetched = True
                    return {"totalPages": usnews['data']['totalPages'], "head": header_selected}
            except:
                pass


    def __save_rest(self, length, head):
        for page in range(2, length+1):
            url = self.api+"&_page="+str(page)
            try:
                page_raw = requests.get(url=url, headers=head, timeout=3)
                if page_raw.status_code == 200:
                    page_data = page_raw.json()
                    with open("apidata/"+str(page)+".json", 'w') as f:
                        json.dump(page_data, f)
            except:
                pass


    def __read_json(self, filepath):
        with open(filepath, 'r') as fp:
                return json.load(fp)


    def __check_directory(self, dirname):
        if not os.path.exists(dirname):
            os.makedirs(dirname)
            initials = self.__save_initial()
            head = initials["head"]
            self.__save_rest(initials['totalPages'], head)


    def get_usa(self):
        dirname = 'apidata'
        self.__check_directory(dirname)
        complete_list = list()
        files = [int(i.split('/')[1].split('.')[0]) for i in glob(dirname+"/*.json")]
        for num in sorted(files):
            apifile = dirname+"/"+str(num)+".json"
            file_json = self.__read_json(apifile)
            file_data = file_json["data"]
            for item in file_data["items"]:
                out = dict()
                detail = item["institution"]
                item_keys = ["displayName", "rankingDisplayRank", "state", "city", "zip"]
                for key in item_keys:
                    out[key] = detail[key]
                out["description"] = desc = item["blurb"]
                if desc.startswith("<p>"):
                    out["description"] = desc[3:-4]
                complete_list.append(out)
        return complete_list


    def save_json(self, inplist, filename):
        if inplist != []:
            with open(filename, 'w') as fh:
                fh.write(json.dumps(inplist, indent=4))


    def save_csv(self, inplist, filename):
        if inplist != []:
            df = pd.DataFrame(inplist)
            df.to_csv(filename, index=False)

    
    def _connection(self):
        try:
            ua = self.__useragent()
            headers = {"User-Agent": ua}
            data = requests.get(url=self.api, headers=headers, timeout=3)
            return data.status_code
        except:
            return 404