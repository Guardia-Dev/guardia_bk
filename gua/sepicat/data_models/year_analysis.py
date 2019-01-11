# search date range syntax
# https://help.github.com/articles/understanding-the-search-syntax/
#
# search API
# https://developer.github.com/v3/search/
#
# commits 请求
# https://api.github.com/search/commits?q=committer:Desgard committer-date:2018-01-01..2018-12-31


class YearAnalysis:

    def __init__(self, login, token, year):
        self.login = login
        self.token = token
        self.year = year


