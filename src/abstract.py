from abc import ABC, abstractmethod


class Vacancy(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancy(self):
        """
        Получает список вакансий
        """
        pass

    @abstractmethod
    def get_requests(self):
        """
        Выполняет запрос по заданным параметрам
        """
        pass

    @abstractmethod
    def parsing(self, data_list):
        """
        Парсит данные для пользователя
        """
        pass

    @ def get_salary(self, salary):
        """
        Преобразовывает в нужный вид параметр salary
        """
        pass
