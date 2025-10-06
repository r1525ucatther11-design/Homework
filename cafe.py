from functools import reduce

# 1 функция- Добавить или обновить блюдо
def add_eat():
    name = input("Название блюда для добавления/обновления: ").strip()
    try:
        price = int(input("Цена блюда: "))
    except:
        print("Ошибка! Введите число для цены блюда.")
        return 
    menu_cafe.update({name: price}) # добавляем или обновляем блюдо в словаре меню
    print(f"{name} добавлено.")


# 2 функция - Удалить блюдо
def delete_eat():
    name = input("Название блюда для удаления: ").strip()
    if name in menu_cafe:
        del menu_cafe[name]  # удаляем элемент по ключу
        print(f"{name} удалено из меню.")
    else:
        print("Такого блюда нет!")

# 3 функция - Показать меню по названию (алфавит)
def sort_name():
    if not menu_cafe:
        print("Меню пустое!")
        return
    print("\nМеню по названию:")

    for item in sorted(menu_cafe.items(), key=lambda item: item[0]): # сортируем по названию блюда с помощью sorted и lambda
        name = item[0]   # ключ словаря — название блюда
        price = item[1]  # значение словаря — цена
        print(f"{name} — {price} руб.")

# 4 - Показать меню по цене
def sort_price():
    if not menu_cafe:
        print("Меню пустое!")
        return
    print("\nМеню по цене:")

    for item in sorted(menu_cafe.items(), key=lambda item: item[1]): #так же, только с ценой
        name = item[0]   # ключ словаря — название блюда
        price = item[1]  # значение словаря — цена
        print(f"{name} — {price} руб.")

# 5 - Средняя цена блюда
def average_price():
    if not menu_cafe:
        print("Меню пустое!")
        return
    prices = list(map(lambda x: x, menu_cafe.values())) # получаем список всех цен
    avg = sum(prices) / len(prices) # сумму на длину = среднее
    print("\nСредняя цена блюда:", avg, "руб.")

# 6 - Блюда дешевле N
def cheaper_than():
    if not menu_cafe:
        print("Меню пустое!")
        return
    try:
        n = int(input("Показать блюда дешевле: "))
    except:
        print("Ошибка! Введите число.")
        return 

    cheap = list(filter(lambda x: x[1] < n, menu_cafe.items())) # фильтруем блюда дешевле N
    print("Блюда дешевле", n, "руб.:")
    for item in cheap:
        print(item[0], "-", item[1], "руб.") # фильтруем блюда дешевле N

# 7 - Самое дешевое и самое дорогое блюдо
def min_max_price():
    if not menu_cafe:
        print("Меню пустое")
        return
    min_price = min(menu_cafe.items(), key=lambda x: x[1]) # дешевое находим блюдо
    max_price = max(menu_cafe.items(), key=lambda x: x[1]) # дорогое находим блюдо
    print(f"Самое дешевое: {min_price[0]} — {min_price[1]} руб.")
    print(f"Самое дорогое: {max_price[0]} — {max_price[1]} руб.")

# 8 - Список напитков
def drinks_list():
    
    drinks = [("coffee", 120), ("tea", 80), ("juice", 100)]

    drinks_filtered = filter(lambda d: d[0] in ["coffee", "tea", "juice"], drinks)

    # сортируем напитки по цене (d[1] — это цена)
    drinks_sorted = sorted(drinks_filtered, key=lambda d: d[1])

    print("\nНапитки по цене:")
    for name, price in drinks_sorted:
        print(name, "-", price, "руб.")

# 9 - Сформировать заказ
def create_order():
    order_input = input("Введите блюда через запятую: ")
    
    items = list(map(lambda x: x.strip(), order_input.split(","))) # убираем пробелы у каждого блюда

    valid_items = list(filter(lambda x: x in menu_cafe, items)) # оставляем только существующие в меню блюда

    if not valid_items:
        print("Вы ничего не выбрали.")
        return

    order = list(map(lambda x: (x, menu_cafe[x]), valid_items)) # формируем словарь заказа {название: цена}

    show_order(order) # вызываем функцию показа заказа


# 10, 11, 12 задания
def show_order(order):
    if not any(order):
        print("Вы ничего не выбрали.")
        return

    print("\nВаш заказ:")

    for i, (name, price) in enumerate(order, start=1): # нумеруем блюда
        print(i, "-", name, "-", price, "руб.")

    sum_order = reduce(lambda total, item: total + item[1], order, 0) # считаем общую сумму через reduce

    if sum_order > 500:
        sum_order *= 0.9  # применяем скидку 10%
        print("Сумма заказа больше 500 рублей. Применена скидка 10%!")

    print("Итого к оплате:", int(sum_order), "руб.")


menu_cafe = {}

menu_actions = {
    "1": add_eat,
    "2": delete_eat,
    "3": sort_name,
    "4": sort_price,
    "5": average_price,
    "6": cheaper_than,
    "7": min_max_price,
    "8": drinks_list,
    "9": create_order,
    "0": exit
}

def main():
    while True:
        print("\nМеню действий:")
        print("1 - Добавить/обновить блюдо")
        print("2 - Удалить блюдо")
        print("3 - Показать меню по названию")
        print("4 - Показать меню по цене")
        print("5 - Показать среднюю цену блюда")
        print("6 - Показать блюда дешевле N")
        print("7 - Показать самое дешевое и самое дорогое блюдо")
        print("8 - Показать список напитков")
        print("9 - Сделать заказ")
        print("0 - Выйти")
        
        choice = input("Выберите пункт: ").strip()
        act = menu_actions.get(choice)
        if act:
            act()
        else:
            print("Неверный выбор. Попробуйте снова.")

main()
