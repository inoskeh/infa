import random
import os
import string

def print_char_list(array):
    for char in array:
        print(char)

def task1():
    n = int(input("Введите количество элементов массива: "))
    array = []
    for i in range(n):
        char = input(f"Введите символ #{i+1}: ")
        array.append(char)
    print("Последовательность символов:", array)

    symbol = input("Введите символ для проверки вхождения: ")
    proverka1(array, symbol)

    first_symbol = input("Введите первый символ для проверки пары: ")
    second_symbol = input("Введите второй символ для проверки пары: ")
    proverka2(array, first_symbol, second_symbol)

    proverka3(array)
    proverka4(array)
    proverka5(array)

def proverka1(array, symbol):
    if symbol in array:
        print(f"Символ \"{symbol}\" входит в последовательность {array}")
    else:
        print(f"Символ \"{symbol}\" не входит в последовательность {array}")

def proverka2(array, first_symbol, second_symbol):
    pairs_count = 0
    for i in range(len(array)-1):
        if array[i] == first_symbol and array[i+1] == second_symbol:
            pairs_count += 1
    print(f"Количество пар символов \"{first_symbol}{second_symbol}\": {pairs_count}")

def proverka3(array):
    pairs_count = 0
    for i in range(len(array)-1):
        if array[i] == array[i+1]:
            pairs_count += 1
    print(f"Количество пар одинаковых символов: {pairs_count}")

def proverka4(array):
    for i in range(1, len(array)-2):
        if array[i] == array[i+1] and array[i-1] == array[i+2]:
            print("Существуют такие i и j, что 1 < i < j < n и si совпадает с si+1, а sj с sj+1.")
            return
    print("Такие i и j не существует.")

def proverka5(array):
    space_count = array.count(" ")
    print(f"Количество пробелов в массиве: {space_count}")

def task3():
    for i in range(5):
        print("Введите текст:")
        text = input()
        with open("file.txt", "a") as file:
            file.write(text + "\n")


def print_string_list(array):
    for item in array:
        print(item)

def random_choice(array):
    return random.choice(array)

def task4():
    array = [
        "https://vk.com/id441822698",
        "https://github.com/inoskeh/infa/tree/main/labs",
        "https://do.pstu.ru/mod/assign/view.php?id=45010",
        "https://music.yandex.ru/home",
        "https://www.youtube.com/",
        "https://www.twitch.tv/",
        "https://ya.ru/",
        "https://www.google.ru/drive/",
        "www.example9.com",
        "www.example10.com"
    ]

    print_string_list(array)
    input("Для получения случайного элемента массива нажмите Enter:")
    random_item = random_choice(array)
    print(random_item)
    input("Для продолжения нажмите Enter:")

def task5():
    print("Введите текст:")
    text = input()

    with open('task1.out', 'w') as file:
        file.write(text)

def task7():
    extensions = ["txt", "csv", "jpg", "png", "doc", "xls"]  # Замените это на ввод с консоли, если требуется

    # Создание директорий
    for extension in extensions:
        try:
            os.makedirs(extension)
        except FileExistsError:
            pass

    # Создание и перемещение файлов
    for _ in range(10):
        extension = random.choice(extensions)
        filename = ''.join(random.choices(string.ascii_lowercase, k=5)) + '.' + extension
        with open(filename, 'w') as file:
            pass
        os.rename(filename, os.path.join(extension, filename))

    # Вывод списка файлов
    files = []
    for extension in extensions:
        files.extend([f"{extension}/{file}" for file in os.listdir(extension)])

    print("Список файлов:")
    for file in files:
        print(file)

    input("Нажмите любую клавишу для переноса файлов ...")


task7()
