from src.entities.hh_api import HeadHunterAPI
from src.entities.sj_api import SuperJobAPI
from src.entities.JSONServise import JSONService
from src.utils import sort_data, get_top


def main():
    # Создаем экземпляры класса для работы с API
    hh_vac = HeadHunterAPI('Python')
    sj_vac = SuperJobAPI('Python')

    # Получение вакансий с разных платформ
    hh_vacancies = hh_vac.get_vacancy()
    superjob_vacancies = sj_vac.get_vacancy()

    # Сохранение информации о вакансиях в файл
    json_service = JSONService('vacancies/vacancies_list.json')
    json_service._connect('vacancies/vacancies_list.json')
    json_service.clear_data()

    all_vacancies = hh_vacancies + superjob_vacancies

    for job in all_vacancies:
        json_service.insert(job.__dict__)

    source = input("С каким источником работаем (HH, SJ или all)?\n ")
    vacancy = all_vacancies
    if source.lower() == 'hh':
        vacancy = hh_vacancies
    elif source.lower() == 'sj':
        vacancy = superjob_vacancies
    elif source.lower() == 'all':
        vacancy = all_vacancies
    else:
        print('Такого источника нет, вывод по умолчанию "all"')

    while True:
        command = input("Введите команду (sort, top): ")

        if command == 'sort':
            sorted_vacancies = sort_data(vacancy)
            for job in sorted_vacancies:
                print(job)

        elif command == 'top':

            top_count = int(input('Введите кол-во вакансий: '))

            top_vacansies = get_top(vacancy, top_count)
            for job in top_vacansies:
                print(job)

        actions = input("Что будем делать с вакансиями (del, select, ничего)?\n")

        if actions == 'del':
            del_id = input('Введите id вакансии: ')
            json_service.delete(del_id)

        elif actions == 'select':
            select_id = input('Введите id вакансии: ')
            print(json_service.select(select_id))

        elif actions.lower() == 'ничего':
            break

        else:
            print("Такой команды нет")
            continue

        continue_program = input('Хотите продолжить программу? (y/n): ')

        if continue_program.lower() == "n":
            print('До новых встреч!')
            break
        elif continue_program not in ['y', 'n']:
            print('Некорректный ответ')
            break


if __name__ == '__main__':
    main()
