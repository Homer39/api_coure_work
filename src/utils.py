from src.entities.vacancy import Vacancy


def sort_data(all_vacancies: list[Vacancy]) -> list[Vacancy]:
    return sorted(all_vacancies, reverse=True)


def get_top(all_vacancies: list[Vacancy], num: int) -> list[Vacancy]:
    return sorted(all_vacancies, reverse=True)[:num]
