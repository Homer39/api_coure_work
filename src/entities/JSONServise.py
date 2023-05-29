import os
import json
from src.entities.abstract import JSON


class FileManagerMixin:

    @staticmethod
    def _connect(filename) -> None:
        """
        Если папка и файл для записи данных не существует, то создает их
        """

        if not os.path.exists(os.path.dirname(filename)):
            os.mkdir(os.path.dirname(filename))

        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                file.write(json.dumps([]))

    @staticmethod
    def _open_file(filename) -> list:

        with open(filename, 'r', encoding="utf-8") as file:
            return json.load(file)


class JSONService(FileManagerMixin, JSON):

    def __init__(self, file_path) -> None:
        self.__data_file = file_path

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        self.__data_file = value
        self._connect(self.__data_file)

    def insert(self, data) -> None:
        """
        Записывает данные в файл
        """
        file_data = self._open_file(self.__data_file)
        file_data.append(data)

        with open(self.__data_file, 'w', encoding='utf-8') as file:
            json.dump(file_data, file, indent=4, ensure_ascii=False)

    def select(self, id=None) -> list:
        """
        Выбирает данные из файла по заданным критериям
        """
        file_data = self._open_file(self.__data_file)

        if not id:
            return file_data

        result = []
        for item in file_data:
            if id == item['id']:
                result.append(item)

        return result

    def delete(self, id=None) -> None:
        """
        Удаляет данные из файла по id
        """
        file_data = self._open_file(self.__data_file)

        if not id:
            return

        result = []
        for entry in file_data:
            if id != entry['id']:
                result.append(entry)

        with open(self.__data_file, 'w', encoding='utf-8') as file:
            json.dump(result, file, indent=4, ensure_ascii=False)

    def clear_data(self):
        """
        Очищает файл
        """
        with open(self.__data_file, 'w') as file:
            file.write(json.dumps([]))
