# fetch the state and state emoji

from bs4 import BeautifulSoup
import bs4
import re
import requests
import copy

USER_HTML = "https://github.com/{login}"

class Getoutloop(Exception):
    pass

def fetch_state(login: str, header: dict = {}) -> dict:
    url = USER_HTML.format(login=login)
    if len(header) <= 0:
        resp = requests.get(url)
    else:
        resp = requests.get(url, header=header)
    html_str = resp.content
    # print(html_str)
    res = {}
    soup = BeautifulSoup(html_str, 'lxml')

    try:
        # 先判断是否有 GitHub 自定义 emoji
        emoji_element = soup.find("img", attrs={
            "class": "emoji",
        })
        if emoji_element is not None:
            icon = emoji_element.attrs['src']
            emoji_title = emoji_element.attrs['title']
            title = ''
            state_text = ''
            raise Getoutloop

        # 判断常规的 emoji 类型
        emoji_element = soup.find("g-emoji", attrs={
            "class": "g-emoji",
        })
        parent_element = soup.find("div", attrs={
            "class": "float-left ws-normal text-gray-dark text-bold",
        })
        if emoji_element is not None and parent_element is not None:
            icon = emoji_element.attrs['fallback-src']
            emoji_title = ''
            title = parent_element.text.strip()
            state_text = parent_element.text.strip()
            raise Getoutloop

        # 没有状态节点
        if emoji_element is not None:
            icon = emoji_element.attrs['fallback-src']
            emoji_title = ''
            title = ''
            state_text = ''
            raise  Getoutloop

    except Getoutloop:
        state_title = soup.find("div", attrs={
            "class": re.compile(r'^[\s\S]*?user-status-message-wrapper.+?$')
        })
        res['state'] = {
            'icon': icon,
            'title': title,
            'state_text': state_text,
            'text': state_title.findChild().text,
        }

        return res

if __name__ == "__main__":
    # login = "Desgard"
    # login = "derekcoder"
    login = 'dreampiggy'
    print(fetch_state(login=login))
