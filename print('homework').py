import csv

students = {}

# Функция 1: "Добавить студента"
def add_student():
    name = input("Имя студента: ").strip()
    if not name.isalpha():  # проверяем, что имя состоит только из букв
        print("Ошибка: Имя должно содержать только буквы!")
        return 

    try:
        age = int(input("Возраст: ").strip())
        
        grades_input = input("Оценки через пробел: ").strip()
        grades = []
        for g in grades_input.split():  # проходим по каждому слову из ввода
            grades.append(int(g))  # превращаем строку в число и добавляем в список
        
        students[name] = {"age": age, "grades": grades}  # создан словарь добавляем студента
        print(name, "добавлен.")
    except:
        print("Ошибка при вводе данных!")


# Функция 2: "Показать всех студентов""
def show_students():
    if not students:
        print("Список студентов пуст.")
        return
    for name in students:
        print(name, students[name])


# Функция 3: "Поиск студентов"
def find_student():
    name = input("Кого ищем? ").strip()
    for n in students:
        if n == name:
            print(n, students[n])
            break  # останавливаем цикл, студент найден
    else:
        print("Не найдено.")


# Функция 4: "Удалить студента"
def delete_student():
    name = input("Кого удалить? ").strip()
    if name in students:
        del students[name] # через дел удаляем студента
        print(name, "удален.")
    else:
        print("Не найдено.")


# Функция 5: "Добавить оценку"
def add_grade():
    name = input("Кому добавить оценку? ").strip()  # вводим имя студента
    if name not in students:
        print("Не найдено.")
        return

    grade_input = input("Оценка: ").strip()
    if grade_input.isdigit():  # проверяем, что введено число
        students[name]["grades"].append(int(grade_input))  # добавляем оценку
        print("Добавлено.")
    else:
        print("Ошибка с оценкой!")


# Функция 6: "Студенты старше"
def students_older():
    age_input = input("Введите определённый возраст: ").strip()
    if not age_input.isdigit():  # проверяем, что введённое значение число
        print("Введите возраст числом.")
        return

    age_limit = int(age_input)
    for name in students:
        if students[name]["age"] > age_limit:  # проверяем, старше ли студент заданного возраста
            print(name, students[name])
    else:
        if all(students[n]["age"] <= age_limit for n in students): # если все студенты меньше или равны опред возврасту, то не найден
            print("Такой студент не найден!")


# Функция 7: "Студенты с оценкой выше"
def students_with_high_grades():
    try:
        min_grade = int(input("Порог оценки: ").strip())
        found_students = []  # создаю новый список
        for name in students:
            info = students[name]
            if max(info["grades"]) > min_grade: # если хотя бы одна оценка студента выше порога, добавляем его в список
                found_students.append((name, info))  # добавляем этого студента в список

        if found_students:  # если список не пустой
            for name, info in found_students:
                print(name, info)
        else:  # если список пустой
            print("Нет таких студентов.")
    except:
        print("Ошибка ввода!")

# Функция 8: "Сохранить TXT"
def export_txt():
    try:
        with open("students.txt", "w", encoding="utf-8") as file: # w - write - читать, а encoding - указывает кодировку файла. UTF-8 — стандартная кодировка, которая поддерживает русские буквы и специальные символы.
            for name in students:
                info = students[name]
                grades_str = " ".join(map(str, info["grades"]))  # превращаем список оценок в строку через пробел
                file.write(f"Имя: {name}, Возраст: {info['age']}, Оценки: {grades_str}\n") # записываем в файл инфу о студенте
        print("Данные успешно сохранены в students.txt")
    except:
        print("Ошибка при сохранении данных!")

# Функция 9: "Загрузить TXT"
def import_txt():
    try:
        with open("students.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаем пустые строки

                name_part, age_part, grades_part = line.split(", ")

                name = name_part.split(": ")[1]   # получаем имя, начинаем с [1], так как [0] - это будет "Имя", а [2] - например, "Катя"
                age = int(age_part.split(": ")[1])  # получаем возраст
                grades = list(map(int, grades_part.split(": ")[1].split()))  # получаем оценки

                students[name] = {"age": age, "grades": grades}

        print("Данные загружены из students.txt")
    except:
        print("Ошибка при загрузке!")


# МЕНЮ
menu = { #словарь из всех наших функций
    "1": add_student,
    "2": show_students,
    "3": find_student,
    "4": delete_student,
    "5": add_grade,
    "6": students_older,
    "7": students_with_high_grades,
    "8": export_txt,
    "9": import_txt,
    "0": exit
}

# Функция 10: "Создаем меню"
def main():
    while True:  # бесконечный цикл меню пока пользователь не выберет выход

        print("\nМеню:")
        print("1 - Добавить студента.")
        print("2 - Показать всех студентов.")
        print("3 - Найти студента.")
        print("4 - Удалить студента.")
        print("5 - Добавить оценку.")
        print("6 - Студенты старше опред.возраста.")
        print("7 - Студенты с высшей оценкой.")
        print("8 - Сохранить TXT.")
        print("9 - Загрузить TXT.")
        print("0 - Выход.")

        choice = input("Выберите пункт: ").strip()
        act = menu.get(choice)  # ищет значение в словаре menu по ключу choice
        if act:  # если номер корректный
            act()  # то выбор совершается
        else:
            print("Неверно!")
main()
