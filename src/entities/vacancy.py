from src.entities.abstract import Vacancies


class Vacancy(Vacancies):

    def __init__(self, id, title, url, salary_from, salary_to, currency, employer, api):
        self.id = id
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.employer = employer
        self.api = api

    @property
    def salary(self) -> int:
        """
        Высчитывает среднюю зп
        """
        salary = int((self.salary_from + self.salary_to) / 2)
        return salary

    def __gt__(self, other) -> bool:
        """
        Производит сравнение вакансий по зп
        """
        return self.salary > other.salary

    def __lt__(self, other) -> bool:
        """
        Производит сравнение вакансий по зп
        """
        if other.salary is None:
            return False
        if self.salary is None:
            return True

        return self.salary < other.salary

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.title}, {self.url}, {self.salary}, ' \
               f'{self.currency}, {self.employer}, {self.api})'
