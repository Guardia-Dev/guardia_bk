
class Contribution:
    """
    个人贡献度
    """

    def __init__(self, count, date, level):
        self.count = count
        self.date = date
        self.level = level

    @property
    def to_dict(self):
        return {
            'count': self.count,
            'date': self.date,
            'level': self.level,
        }

class RepoActivity:
    """
    仓库贡献程度
    """

    def __init__(self, repo_name):
        self.repo_name = repo_name
        self.commit_cnt = 0
        self.pull_request_cnt = 0
        self.issue_cnt = 0
        self.is_created = False