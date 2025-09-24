fruits_input = input("Введите фрукты через запятую: ")

fruits_list = []
for fruit in fruits_input.split(","):
    clean_fruit = fruit.strip().capitalize() #удаляем пробелы и каждому слову первую букву делаем заглавной / 1, 2, 3 пункт
    fruits_list.append(clean_fruit)

fruits_list = sorted(list(set(fruits_list))) # убираем повторы с помощью множества и сортируем по алфавиту / 4, 5 пункт

print("Список фруктов без повторов и по алфавиту:", fruits_list)


fruits_original = [fruit.strip().capitalize() for fruit in fruits_input.split(",")]
most_popular = max(fruits_original, key = fruits_original.count) # 7 пункт: найти самый популярный фрукт
print("Самый популярный фрукт:", most_popular)

fruits_list = {} #словарь с количеством повторов фруктов / 6 пункт
for fruit in fruits_original:
    if fruit in fruits_list:
        fruits_list[fruit] += 1
    else:
        fruits_list[fruit] = 1

print("Словарь фруктов и их количества:", fruits_list)

fruits_tuple = tuple(fruits_list) # 8 пункт: сделать кортеж из всех уникальных фруктов
print("Кортеж из уникальных фруктов:", fruits_tuple)

for check_fruit in ["Banana", "Mango", "Pineapple"]: # 9 пункт: проверить наличие Banana, Mango, Pineapple
    if check_fruit in fruits_list:
        print(check_fruit, "есть в списке фруктов.")
    else:
        print(check_fruit, "нет в списке фруктов.")

# 10 пункт: спросить число N и вывести первые N фруктов в алфавитном порядке
N = int(input("Сколько фруктов вывести? Введите число N: "))
print("Первые N фруктов в алфавитном порядке:", sorted(list(set(fruits_original)))[:N])
