import requests
from src.entities.abstract import Api
from src.entities.vacancy import Vacancy


class VacancyError(Exception):
    pass


class HeadHunterAPI(Api):

    def __init__(self, keyword: str) -> None:
        self.__params = {'text': f'NAME: {keyword}',
                         'page': 0,
                         'per_page': 100}

    def get_vacancy(self) -> list:
        """
        Получает список вакансий
        """
        try:
            vac_list = self.get_requests()
        except VacancyError:
            print('Oшибка данных')
        else:
            return self.parsing(vac_list)

    def get_requests(self) -> list:
        """
        Выполняет запрос по заданным параметрам
        """
        response = requests.get('https://api.hh.ru/vacancies', params=self.__params)
        if response.status_code != 200:
            raise VacancyError('Oшибка данных')
        return response.json()['items']

    def parsing(self, vac_list: list) -> list:
        """
        Парсит данные для пользователя
        """
        vacansies = []
        for vac in vac_list:
            salary_from, salary_to, currency = self.get_salary(vac['salary'])
            vacancy = Vacancy(vac['id'],
                              vac['name'],
                              vac['alternate_url'],
                              salary_from,
                              salary_to,
                              currency,
                              vac['employer']['name'],
                              'hh')
            vacansies.append(vacancy)
        return vacansies

    def get_salary(self, salary: dict) -> list:
        """
        Преобразовывает в нужный вид параметр salary
        """
        new_salary = [0, 0, None]
        if salary and salary['from']:
            new_salary[0] = salary['from']
            new_salary[2] = salary['currency']
        if salary and salary['to']:
            new_salary[1] = salary['to']
        return new_salary


