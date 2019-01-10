
class YearAnalysis:

    def __init__(self, login, token, year):
        self.login = login
        self.token = token
        self.year = year

    def description(self):
        return "{login}'s analysis in {year}".format(login=self.login, year=self.year)

