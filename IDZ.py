# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import json
import sys
from datetime import date


def get_worker():
    surname = input("Фамилия: ")
    name = input("Имя: ")
    zodiac = input("Знак зодиака: ")
    date_obj = input("Дата: ").split('.')

    return {
        'surname': surname,
        'name': name,
        'zodiac': zodiac,
        'date_obj': date_obj,
    }


def display_workers(staff):
    if staff:

        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 15,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^15} | {:^20} |'.format(
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
                '| {:^4} | {:^30} | {:^20} | {:^15} | {:^20} |'.format(
                    idx,
                    worker.get('surname', ''),
                    worker.get('name', ''),
                    worker.get('zodiac', ''),
                    str(worker.get('date_obj', '')),
                )
            )
        print(line)

    else:
        print("Список пуст.")


def save_workers(file_name, staff):
    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(staff, fout, ensure_ascii=False, indent=4)


def load_workers(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
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

        elif command.startswith("save "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            save_workers(file_name, workers)

        elif command.startswith("load "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            workers = load_workers(file_name)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить работника;")
            print("list - вывести список работников;")
            print("help - отобразить справку;")
            print("load - загрузить данные из файла;")
            print("save - сохранить данные из файла;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
