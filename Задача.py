class Profile :
    def __init__(self, name):
        self.name = name

    def info(self):
        return ''

    def describe(self):
        print(self.name)
        print(self.info)


class Vacancy(Profile):
    def __init__(self, name, date):
        super().__init__(name)
        self.name = name
        self.date = date

    def info(self):
        return f'Предлагаемая зарплата: {self.date}'

    def subscribe(self, user):
        pass


class Resume(Profile):
    def __init__(self, name, about):
        super().__init__(name)
        self.name = name
        self.about = about

    def info(self):
        return f'Стаж работы: {self.about}'