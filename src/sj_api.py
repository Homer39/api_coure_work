import requests
from src.abstract import Vacancy
import os


class VacancyError(Exception):
    pass


class SuperJobAPI(Vacancy):
    api_key = os.getenv('API_KEY_Super_Job')

    def __init__(self, keyword):
        self.__params = {'keywords': {keyword},
                         'town': 'Москва',
                         'sort_new (unixtime)': 1,
                         'page': 1,
                         'count': 20}
        self.__vacancies = []

    def get_requests(self):
        """
        Выполняет запрос по заданным параметрам
        """
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers={'X-Api-App-Id': SuperJobAPI.api_key},
                                params=self.__params)
        if response.status_code != 200:
            raise VacancyError('Oшибка данных')
        return response.json()['objects']

    def get_vacancy(self):
        """
        Получает список вакансий
        """
        try:
            vac_list = self.get_requests()
        except VacancyError:
            print('Oшибка данных')
        else:
            self.__vacancies.extend(vac_list)
            print(f'Количество вакансий - {len(self.__vacancies)}')
            print(self.__vacancies)


Sj_vac = SuperJobAPI('Python')
Sj_vac.get_vacancy()
