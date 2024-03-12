from urllib import request

import requests

kw = {'wd': '中国'}

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

response = requests.get("https://www.luogu.com.cn/problem/P1102" ,headers=headers)

print(response.text)