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
    soup = BeautifulSoup(html_str, 'lxml')


if __name__ == "__main__":
    login = "Desgard"
    print(fetch_state(login=login))
