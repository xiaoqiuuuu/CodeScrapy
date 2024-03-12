import time
import os
from MyRequest import *
from QuerySql import *

import threading
import json

code_cnt = 0
code_count = 0

def create_thread(row):
    global thread_count
    global thread_count_lock
    global code_cnt
    global code_count


    with thread_count_lock:
        print(f'正在爬取{row}')

    dir_name = ""
    for c in row[1]:
        if c.isdigit():
            dir_name += c
        else:
            break

    detail = {"name": "CF" + row[1],
              "title": row[2],
              "tag": row[3].split(" "),
              "rating": row[4],
              "acNum": row[5],
              "problemUrl": f"https://codeforces.com/problemset/problem/{dir_name}/{row[1][len(dir_name):]}",
              "acCodeUrl": f"https://codeforces.com/problemset/status/{dir_name}/problem/{row[1][len(dir_name):]}"
              }

    try:
        os.makedirs(os.path.join(f"CF{dir_name}/{row[1]}", "cpp"))
    except FileExistsError:
        print("Directory already exists")

    def quit_threading():
        global thread_count
        with thread_count_lock:
            thread_count -= 1

    def write_wrong():
        with thread_count_lock:
            with open("wrong.txt", "a") as wr:
                wr.write(str(row) + "\n")

    if len(os.listdir(f"CF{dir_name}/{row[1]}/cpp")):
        quit_threading()
        return

    try:
        solutions_id = get_solutions_id(detail["acCodeUrl"])
    except:
        quit_threading()
        write_wrong()
        return

    if solutions_id is None:
        write_wrong()
        quit_threading()
        return

    i = 0
    for solution_id in solutions_id:
        try:
            text = get_source_code(dir_name, solution_id[0])
        except:
            continue
        i += 1
        name = "solution{:2d}".format(i)


        ok = 0
        with thread_count_lock:
            try:
                with open(f"CF{dir_name}/{row[1]}/cpp/{name}.cpp", "w", encoding='utf-8') as cpp:
                    cpp.write(text)
            except:
                try:
                    with open(f"CF{dir_name}/{row[1]}/cpp/{name}.cpp", "w", encoding='ANSI') as cpp:
                        cpp.write(text)
                except:
                    pass
                else:
                    ok = 1
            else:
                ok = 1
        if ok:
            code_count += 1
            print(f"成功爬取{code_count}份代码")

        time.sleep(random.randint(0, 2) + random.random())

    with thread_count_lock:
        detail["codeNum"] = i
        with open(f"CF{dir_name}/{row[1]}/detail.json", "w", encoding='utf-8') as js:
            json.dump(detail, js)
        code_cnt += 1
        print(f'{row}爬取完成，共爬取了{code_cnt}个题目 ')
    quit_threading()


if __name__ == "__main__":
    basedir = r"E:\CodeData"
    os.chdir(basedir)

    # 创建一个锁对象，用于线程安全地修改线程计数
    thread_count_lock = threading.Lock()
    thread_count = 0

    database = QuerySql()

    problems_list = database.query()

    i = 0
    while i < len(problems_list):
        with thread_count_lock:
            print(f"当前线程数量{thread_count}")
            if thread_count >= 12:
                time.sleep(5)
            else:
                thread_count += 1
                threading.Thread(target=create_thread, args=(problems_list[i],)).start()
                i += 1

    database.close()
