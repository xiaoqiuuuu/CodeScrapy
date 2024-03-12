"""
 爬取CF所有题目的编号和标签
"""

import time

import requests
from bs4 import BeautifulSoup

import pymysql


class Problem:
    def __init__(self, Index: str, Name: str, Tag: [], Rating: int, Ac_num: int):
        self.id = Index
        self.name = Name
        self.tag = Tag
        self.rating = Rating
        self.ac_num = Ac_num

    def __str__(self):
        return f'\"{self.id}\",\"{self.name}\",{" ".join(self.tag)},{self.rating},{self.ac_num}'


conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Weiqt",
    database="cf_problems"
)

cursor = conn.cursor()
sql = """INSERT INTO problems (remote_id, title, tag, rating, ac_num) 
         VALUES (%s, %s, %s, %s, %s)"""

urls = "https://codeforces.com/problemset/page/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

for page_num in range(1, 95):
    url = urls + str(page_num)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    problems = soup.find_all("table", class_="problems")[0].find_all("tr")
    print(f"正在备份第 {page_num} 页")
    for i in range(1, len(problems)):
        problems_detail = problems[i].find_all("td")
        Id = problems_detail[0].find("a").get_text().strip()
        name = problems_detail[1].find("a").get_text().strip()

        tag = []
        for item in problems_detail[1].find_all("div")[1].find_all("a"):
            tag.append(item.get_text().strip())

        if problems_detail[3].find("span") is None:
            rating = 0
        else:
            rating = int(problems_detail[3].find("span").get_text())

        if problems_detail[4].find("a") is None:
            ac_num = 0
        else:
            ac_num = int(problems_detail[4].find("a").get_text().strip()[1:])

        # 写入数据到数据库
        pr = Problem(Id, name, tag, rating, ac_num)
        values = (pr.id, pr.name, " ".join(pr.tag), pr.rating, pr.ac_num)
        cursor.execute(sql, values)

    conn.commit()
    print(f"第 {page_num} 页已完成")
    time.sleep(2)
cursor.close()
conn.close()