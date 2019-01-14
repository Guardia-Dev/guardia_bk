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

from sepicat.data_models.contribution import Contribution, RepoActivity


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
        if month // 10 == 0:
            month = "0{m}".format(m=month)
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
        self.contributions = []
        self.repo_actions = {}

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
        level_hash_re = {v: k for k, v in level_hash.items()}

        rects = soup.find_all(name="rect")
        self.contributions = []
        for rect in rects:
            current_contribution = Contribution(date=rect.attrs['data-date'],
                                                level=level_hash_re[rect.attrs['fill']],
                                                count=rect.attrs['data-count'])
            self.contributions.append(current_contribution)

    def fetch_commits(self):
        """
        Fetch the commits by GitHub API
        :return:
        """
        self.repo_actions = {}
        for month in range(1, 13):
            print("爬取 {month} 月 Repo Actions".format(month=month))
            html_str = fetch_page(PageType.Contributions,
                                  login=self.login,
                                  header=self.header,
                                  year=self.year,
                                  month=month)
            soup = BeautifulSoup(html_str, 'lxml')
            # 获取全部分类
            outer_types = soup.find_all("div", attrs={
                "class": re.compile(r'profile-rollup-wrapper py-4 pl-4 position-relative ml-3.*?$'),
            })
            month_repo_data = {}
            for outer in outer_types:

                # commits & create repo
                title_ele = outer.find(name="span", attrs={"class": "float-left"})
                if title_ele is not None and type(title_ele) is bs4.element.Tag:
                    title_text = title_ele.text.replace('\n', '')

                    # 类型为 commits
                    if re.match(r'^[\s\S]*Created \d{1,}[\s\S]+commits in.*?$', title_text):
                        items = outer.find_all(name="li", attrs={'class': 'ml-0 py-1'})
                        for item in items:
                            detail = item.text.replace('\n', '')
                            ma = re.match(r'^[\s\S]*?([a-zA-Z0-9\-\.]+/[a-zA-Z0-9\-\.]+)[\s\S]*?(\d{1,})[\s\S]+?commit(:?s)?[\s\S]*$',
                                          detail)
                            if ma:
                                repo_name = ma.group(1)
                                commit_cnt = ma.group(2)
                                if repo_name in month_repo_data.keys():
                                    repo = month_repo_data[repo_name]
                                    repo.commit_cnt += int(commit_cnt)
                                else:
                                    repo = RepoActivity(repo_name=repo_name)
                                    repo.commit_cnt = int(commit_cnt)
                                month_repo_data[repo_name] = repo

                    # 类型为 created repository
                    elif re.match(r'^[\s\S]*?Created[\s\S]*\d{1,}[\s\S]*repositor(y|ies).*?$', title_text):
                        items = outer.find_all(name="li", attrs={'class': 'd-block mt-1 py-1'})
                        for item in items:
                            detail = item.text.replace('\n', '')
                            ma = re.match(r'^[\s\S]*?([A-Za-z0-9\-\.]+/[A-Za-z0-9\-\.]+)[\s\S]+.+$', detail)
                            if ma:
                                repo_name = ma.group(1)
                                if repo_name in month_repo_data.keys():
                                    repo: RepoActivity = month_repo_data[repo_name]
                                    repo.is_created = True
                                else:
                                    repo = RepoActivity(repo_name=repo_name)
                                    repo.is_created = True
                                month_repo_data[repo_name] = repo

            self.repo_actions[month] = month_repo_data


if __name__ == "__main__":
    id = "biboyang"
    analysis = YearAnalysis(login=id, token="", year=2018)
    # analysis.fetch_contributions()
    analysis.fetch_commits()
    # print(analysis.repo_actions)
    tot = 0
    print(id, "的 commit 记录")
    for k, v in analysis.repo_actions.items():
        print(k, "月")
        if type(v) is dict:
            for repo_name, action in v.items():
                if action.commit_cnt == 0:
                    continue
                print(repo_name, "Commit 次数", action.commit_cnt)
                tot += action.commit_cnt

    print("共", tot, "次 Commit 记录")