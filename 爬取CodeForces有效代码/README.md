# 爬取 CodeForces 有效代码

### 项目介绍
为了训练一个C++算法识别模型，决定爬取一些带有标签的 C++ 源代码来进行训练。该项目实现了爬取 CodeForces 题目信息，标签，Rating，通过人数等。
基于爬取的题目信息，爬取每道题目的 AC 代码，并保存到本地中。
### 项目启动
1. 首先配置你本地的mysql，创建数据库，并修改 `app.py` 中代码为你自己的mysql配置。
```angular2html
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Weiqt",
    database="cf_problems"
)
```
2. 运行 `app.py` 文件，即可启动爬虫，这一步是将所有 `ProblemSet` 中的题目信息爬取到数据库中。
3. 爬取每道题目的AC代码：首先先在 `MyRequest.py` 中配置你找的代理，完善其中的 `my_get(url)` 函数。
4. 在 `main.py` 中，配置最大线程数量，项目运行文件夹，即可运行。项目爬取失败的题目会在 `wrong.txt` 中记录。
