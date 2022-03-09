# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import json
import sys
from datetime import datetime


def get_worker():
    surname = input("Фамилия: ")
    name = input("Имя: ")
    zodiac = input("Знак зодиака: ")
    date = input("Дата: ")

    return {
        'surname': surname,
        'name': name,
        'zodiac': zodiac,
        'date': datetime.strptime(date, "%Y-%m-%d")
    }


def display_workers(staff):
    if staff:

        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15,
            '-' * 15
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} | {:^15} |'.format(
                "№",
                "Фамилия",
                "Имя",
                "Знак зодиака",
                "Дата рождения"
            )
        )
        print(line)

        # Вывести данные о всех сотрудниках.
        for idx, worker in enumerate(staff, 1):
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} | {:^15} |'.format(
                    idx,
                    worker.get('surname', ''),
                    worker.get('name', ''),
                    worker.get('zodiac', ''),
                    str(worker.get('date', '').date())
                )
            )
        print(line)

    else:
        print("Список пуст.")


def select_workers(staff):
    month1 = int(input("Введите месяц: "))
    result = []
    for worker in staff:
        if worker.get('date', '').month == month1:
            result.append(worker)
    return result


def save_workers(file_name, staff):
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_workers(file_name):
    with open(file_namr, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    workers = []

    while True:
        command = input(">>> ").lower()
        if command == "exit":
            break
        elif command == "add":
            worker = get_worker()

            workers.append(worker)
            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('name', ''))

        elif command == "list":
            display_workers(workers)

        elif command.startwith("select "):
            parts = command.split(maxsplit=1)
            period = int(parts[1])

            selected = select_workers(workers, period)
            display_workers(selected)

        elif command.startwith("save "):
            parts = command.split(maxplit=1)
            file_name = parts[1]

            save_workers(file_name, workers)

        elif command.startwith("load "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            workers = load_workers(file_name)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("select <стаж> - запрость работников со стажем;")
            print("help - отобразить справку;")
            print("load - загрузить данные из файла;")
            print("save - сохранить данные из файла;")
            print("exit - завершить работу с программой.")

        else: print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()

