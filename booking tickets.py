class NotEnoughMoneyError(Exception):
    pass

def validate_name(name):
    if name.strip() == "":
        raise ValueError("Имя не может быть пустым")
    if not name.isalpha():
        raise ValueError("Имя должно состоять только из букв")
    return name


def validate_age(age):
    try:
        age = int(age)
    except:
        raise ValueError("Возраст должен быть числом")

    if age < 12:
        raise ValueError("Слишком маленький возраст")
    return age


def validate_tickets(count):
    try:
        count = int(count)
    except:
        raise ValueError("Некорректное количество билетов")

    if count <= 0 or count > 5:
        raise ValueError("Некорректное количество билетов")
    return count


def validate_budget(budget):
    try:
        budget = int(budget)
    except:
        raise ValueError("Некорректный бюджет")

    if budget < 0:
        raise ValueError("Некорректный бюджет")
    return budget


def calculate_total(count):
    return count * 500

print("Бронирование билетов")

try:
    name = validate_name(input("Введите ваше имя: "))
    age = validate_age(input("Введите ваш возраст: "))
    amotickets = validate_tickets(input("Какое кол-во билетов вы берете?(1-5): "))
    amomoney = validate_budget(input("Сколько денег вносите?: "))

    total = calculate_total(amotickets)

    if amomoney < total:
        raise NotEnoughMoneyError("Недостаточно денег для оплаты!")

    print("\nВсе данные верны!")
    print(f"Вы успешно приобрели билет на {amotickets} человек(а)!")

except ValueError as e:
    print(f"\nОшибка в данных: {e}")

except NotEnoughMoneyError as e:
    print(f"\nОшибка: {e}")