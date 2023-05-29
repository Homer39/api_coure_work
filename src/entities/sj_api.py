import requests
from src.entities.abstract import Api
from src.entities.vacancy import Vacancy
import os


class VacancyError(Exception):
    pass


class SuperJobAPI(Api):
    api_key = os.getenv('API_KEY_Super_Job')

    def __init__(self, keyword: str) -> None:
        self.__params = {'keywords': {keyword},
                         'town': 'Москва',
                         'sort_new (unixtime)': 1,
                         'page': 1,
                         'count': 5}
        self.__vacancies = []

    def get_requests(self) -> list:
        """
        Выполняет запрос по заданным параметрам
        """
        response = requests.get('https://api.superjob.ru/2.0/vacancies/', headers={'X-Api-App-Id': SuperJobAPI.api_key},
                                params=self.__params)
        if response.status_code != 200:
            raise VacancyError('Oшибка данных')
        return response.json()['objects']

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

    def parsing(self, vac_list: list) -> list:
        """
        Парсит данные для пользователя
        """
        vacansies = []
        for vac in vac_list:
            vacancy = Vacancy(vac['id'],
                              vac['profession'],
                              vac['link'],
                              vac['payment_from'],
                              vac['payment_to'],
                              vac['currency'],
                              vac['firm_name'],
                              'SuperJob')
            vacansies.append(vacancy)
        return vacansies

