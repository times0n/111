def find_duplicates():
    # Вводим список с числами
    input_list = input("Введите числа через пробел: ")
    numbers = list(map(int, input_list.split()))

    # Словарь для хранения дубликатов и их индексов
    index_dict = {}

    # Находим дубликаты
    for index, number in enumerate(numbers):
        if number in index_dict:
            index_dict[number].append(index)
        else:
            index_dict[number] = [index]

    # Выводим дубликаты и их индексы
    duplicates_found = False
    for number, indices in index_dict.items():
        if len(indices) > 1:
            print(f"Число {number} встречается на индексах: {indices}")
            duplicates_found = True 
    if not duplicates_found:
        print("Дубликатов не найдено.")

# Запуск функции
find_duplicates()