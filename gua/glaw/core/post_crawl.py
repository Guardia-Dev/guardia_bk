from bs4 import BeautifulSoup
import bs4
import requests
import re
import json

POST_LIST_API_URL = "https://api.github.com/repos/SwiftGGTeam/source/contents/_posts?ref=master"

def excutor_post():
    # 请求列表
    r = requests.get(POST_LIST_API_URL)
    data_content = r.content
    post_list = json.loads(s=data_content)
    print(post_list)


def resolve_header(raw):
    # 模拟 raw 文件
    r = requests.get("https://raw.githubusercontent.com/SwiftGGTeam/source/master/_posts/20151029_list-comprehensions-and-performance-with-swift.md")
    raw = str(r.content, encoding="utf-8")
    info = {}
    for line in raw.split("\n"):
        # print(line)
        # 匹配 title
        title_re_test = re.match(r'^title:.+?"(.+?)".*?$', line)
        if title_re_test:
            info['title'] = title_re_test.group(1)
        # 匹配时间
        date_re_test = re.match(r'^date:.+?(\d{4}-\d{2}-\d{2}).+?\d{2}:\d{2}:\d{2}.*?$', line)
        if date_re_test:
            info['date'] = date_re_test.group(1)
        # 匹配 categroies
        category_re_test = re.match(r'^permalink:(.+)$', line)
        if category_re_test:
            info['permalink'] = category_re_test.group(1).strip()
        # 匹配 body
        

    print(info)

def resolve_body():
    pass

if __name__ == "__main__":
    # excutor_post()
    resolve_header(None)