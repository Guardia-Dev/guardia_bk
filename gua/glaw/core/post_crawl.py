from bs4 import BeautifulSoup
import bs4
import requests
import re
import json

POST_LIST_API_URL = "https://api.github.com/repos/SwiftGGTeam/source/contents/_posts?ref=master"
TEST_TOKEN = "6614d8f1802af67833d5e9291a652ffc4337ea82"


def excutor_post():
    # 请求列表
    headers = {
        'Authorization': "token 6614d8f1802af67833d5e9291a652ffc4337ea82",
        'cache-control': "no-cache",
    }
    r = requests.get(POST_LIST_API_URL, headers=headers)
    data_content = r.content
    post_list = json.loads(s=data_content)
    # print(post_list)
    ret = []
    if type(post_list) is list:
        for post in post_list:
            if type(post) is dict and 'download_url' in post.keys():
                raw_req = requests.get(post['download_url'])
                raw = str(raw_req.content, encoding="utf-8")
                info = dict(resolve_header(raw))
                info.update(resolve_body(raw))
                ret.append(info)

                # 测试输出
                ptr_post_dict(info)


def resolve_header(raw) -> dict:
    # 模拟 raw 文件
    # r = requests.get("https://raw.githubusercontent.com/SwiftGGTeam/source/master/_posts/20151029_list-comprehensions-and-performance-with-swift.md")
    # raw = str(r.content, encoding="utf-8")
    info = {}
    for line in raw.split("\n"):
        # print(line)
        # 匹配 title
        title_re_test = re.match(r'^title:.+?"(.+?)".*?$', line)
        if title_re_test:
            info['title'] = title_re_test.group(1)
        # 匹配时间
        date_re_test = re.match(r'^date:.+?(\d{4}-\d{2}-\d{2}).*?$', line)
        if date_re_test:
            info['date'] = date_re_test.group(1)
        # 匹配 permalink
        category_re_test = re.match(r'^permalink:(.+)$', line)
        if category_re_test:
            info['permalink'] = category_re_test.group(1).strip()
        # 匹配结束
        body_start_re_test = re.match(r'^---.*?$', line)
        if body_start_re_test:
            break
    # 拼 web_url
    if "date" in info.keys() and "permalink" in info.keys():
        date_split = info['date'].split('-')
        if len(date_split) == 3:
            url_templete = "https://swift.gg/{d1}/{d2}/{d3}/{d4}"
            info['html_url'] = url_templete.format(d1=date_split[0],
                                                   d2=date_split[1],
                                                   d3=date_split[2],
                                                   d4=info['permalink'])

    return info


def resolve_body(raw) -> dict:
    # 模拟 raw 文件
    # r = requests.get("https://raw.githubusercontent.com/SwiftGGTeam/source/master/_posts/20151029_list-comprehensions-and-performance-with-swift.md")
    # raw = str(r.content, encoding="utf-8")
    info, is_body_line = {}, False
    info['body'] = ""
    for line in raw.split("\n"):
        if is_body_line:
            info['body'] += line + '\n'
            continue
        body_start_re_test = re.match(r'^---.*?$', line)
        if body_start_re_test:
            is_body_line = True
    return info


def ptr_post_dict(post: dict):
    print('\n')
    if 'title' in post.keys():
        print("标题：%s" % post['title'])
    if 'date' in post.keys():
        print("发布日期：%s" % post['date'])
    if 'permalink' in post.keys():
        print("后缀：%s" % post['permalink'])
    if 'html_url' in post.keys():
        print("html：%s" % post['html_url'])


if __name__ == "__main__":
    excutor_post()
    print("测试爬虫")
    # resolve_header(None)
    # resolve_body(None)
    pass
