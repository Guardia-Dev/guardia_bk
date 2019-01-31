# fetch the state and state emoji

from bs4 import BeautifulSoup
import bs4
import re
import requests
import copy

USER_HTML = "https://github.com/{login}"

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

    while True:
        # 先判断是否有 GitHub 自定义 emoji
        emoji_element = soup.find("img", attrs={
            "class": "emoji",
        })
        if emoji_element is not None:
            icon = emoji_element.attrs['src']
            title = emoji_element.attrs['title']

    state_title = soup.find("div", re.compile(r'^[\s\S]*?user-status-message-wrapper.+?$'))
    res['state'] = {
        'icon': icon,
        'title': title,
        'text': state_title.findChild().text,
    }

    return res

if __name__ == "__main__":
    login = "Desgard"
    login = "halfrost"
    print(fetch_state(login=login))
