import html
import requests
import time


def change_language(language):
    dic = {"GNU C11": 0,
           "Clang++20 Diagnostics": 0,
           "Clang++17 Diagnostics": 0,
           "C++17 (GCC 7-32)": 0,
           "C++20 (GCC 11-64)": 0,
           "C++20 (GCC 13-64)": 0,
           "MS C++ 2017": 0,
           "C++17 (GCC 9-64)": 0,
           }
    if language in dic:
        return "Cpp"
    return None


def html_to_source(soup):
    # 提取文本内容
    text = soup.get_text()

    # 处理特殊字符
    text = html.unescape(text)

    return text






