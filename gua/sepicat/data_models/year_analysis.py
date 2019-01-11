# search date range syntax
# https://help.github.com/articles/understanding-the-search-syntax/
#
# search API
# https://developer.github.com/v3/search/
#
# commits 请求
# https://api.github.com/search/commits?q=committer:Desgard committer-date:2018-01-01..2018-12-31

from enum import Enum, unique
from bs4 import BeautifulSoup
import bs4
import re
import requests


@unique
class PageType(Enum):
    """
    页面类型
    """
    # Contributions 页面
    Contributions = 0


def fetch_page(tt: PageType, login: str, header: dict, year: int, month: int = 12) -> str:
    """
    Fetch the html by type and params
    :param tt: The type of Page
    :param login: User login name
    :param header: The request header constructed by Analysis
    :param year: The query year
    :param month: The query month
    :return:
    """
    if tt is PageType.Contributions:
        from_date = "{year}-{month}-01".format(year=year, month=month)
        to_date = "{year}-{month}-31".format(year=year, month=month)
        profile_page_url = "https://github.com/{login}?tab=overview&from={from_date}&to={to_date}"
        profile_page_url = profile_page_url.format(login=login, from_date=from_date, to_date=to_date)
        resp = requests.get(profile_page_url, headers=header)
        return resp.content
    return None


class YearAnalysis:

    def __init__(self, login, token, year):
        self.login = login
        self.token = token
        self.year = year
        self.header = {
            # "Authorization": "token {token}".format(token=self.token),
            "Authorization": "token 56fc442a82f3cd5c369468acfef0ae92966e0d3b",
        }

    def fetch_contributions(self):
        """
        Parse contributions rect for current user
        :return:
        """
        html_str = fetch_page(PageType.Contributions,
                              login=self.login,
                              header=self.header,
                              year=self.year)
        soup = BeautifulSoup(html_str, 'lxml')
        # 先解析等级
        level_hash = {}
        legend = soup.find(name="ul", attrs={"class": "legend"}, class_="legend")
        level_rects = list(filter(lambda x: type(x) is not bs4.element.NavigableString, [x for x in legend.children]))
        for level, level_rect in enumerate(level_rects, 1):
            level_style = level_rect.attrs['style']
            # TODO: 这里我用零宽断言一直不生效 r'(?<=background-color: )#[a-fA-F0-9]{6}$', 暂时用捕获
            _r = re.match(r'background-color: (#[a-fA-F0-9]{6})', level_style)
            if _r:
                level_hash[level] = _r.group(1)

        print(level_hash)

        rects = soup.find_all(name="rect")
        for rect in rects:
            pass




if __name__ == "__main__":
    analysis = YearAnalysis(login="Desgard", token="", year=2018)
    analysis.fetch_contributions()
