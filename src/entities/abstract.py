from abc import ABC, abstractmethod


class Api(ABC):

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



class Vacancies(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def salary(self):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass


class JSON(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def insert(self, filepath):
        pass

    @abstractmethod
    def select(self, query):
        pass

    @abstractmethod
    def delete(self, query):
        pass

    @abstractmethod
    def clear_data(self):
        pass
