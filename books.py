books = [
    {"id": 1, "title": "Мастер и Маргарита", "author": "Булгаков", "year": 1966},
    {"id": 2, "title": "Преступление и наказание", "author": "Достоевский", "year": 1866},
    {"id": 3, "title": "Война и мир", "author": "Толстой", "year": 1869},
    {"id": 4, "title": "Анна Каренина", "author": "Толстой", "year": 1877},
    {"id": 5, "title": "Собачье сердце", "author": "Булгаков", "year": 1925}
]

print("1. Найти книгу по названию")
title_input = input("Введите название книги: ")
for book in books:
    if book["title"].lower() == title_input.lower(): # сравниваем введённое название с названием книги (в нижнем регистре, чтобы не зависело от регистра)
        print("Книга", book["title"], "найдена!")
        break
else:
    print("Книга не найдена.")

print("\n2. Найти все книги автора")
author_input = input("Введите имя автора: ")
found_any = False # флаг, чтобы знать, нашли ли хоть одну книгу
for book in books:
    if book["author"].lower() == author_input.lower():
        print(book["title"])
        found_any = True # отмечаем, что хотя бы одна книга найдена
if not found_any: 
    print("  Книг этого автора нет.")

print("\n3. Сортировка книг по году издания")
def bubble_sort_books(arr):
    n = len(arr) # количество элементов
    for i in range(n):
        swapped = False # показывает, происходила ли перестановка
        for j in range(0, n - i - 1):
            if arr[j]["year"] > arr[j + 1]["year"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sorted_books = bubble_sort_books(books[:])  # создаём копию списка, чтобы не менять оригинал

print("  Отсортированные книги по году издания:")
for book in sorted_books:
    print(book["title"] + " (" + str(book["year"]) + ")")


print("\n4. Поиск книг по диапазону лет")
start_year = int(input("Введите начальный год: "))
end_year = int(input("Введите конечный год: "))
found = False
print("  Книги в указанном диапазоне:")
for book in books:
    if start_year <= book["year"] <= end_year: # перебираем все книги и проверяем, попадает ли год в диапазон
        print(book["title"] + " (" + str(book["year"]) + ")") 
        found = True
if not found:
    print("   Книг в этом диапазоне нет.")