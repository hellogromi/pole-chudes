import random

# Список слов для угадывания
word_list = ["яблоко", "груша", "слива", "абрикос", "вишня", "сливовица", "мандарин", "апельсин", "ананас", "лука", "кокос", "кислица", "картошка", "морковь"]

remaining_latters = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
remaining_latters = " ".join(remaining_latters).lower()
remaining_latters = remaining_latters.split()

# Функция для выбора случайного слова
def select_word():
    return random.choice(word_list).lower()

# Функция для отображения загаданного слова с угаданными буквами
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "*"
    return displayed_word

# Функция для проверки ввода
def validate_input(guess):
    if len(guess) > 1:
        return False
    if not guess.isalpha():
        return False
    return True

# Функция для отображения списка команд
def display_commands():
    print("Список команд:")
    print("  !help - показать правила игры и команды")
    print("  !used - показать использованные буквы")
    print("  !remaining - показать оставшиеся буквы")

# Функция для запуска игры
def play_game():
    word = select_word()
    guessed_letters = []
    attempts = 0

    print("Добро пожаловать в игру Виселица!")
    display_commands()
    print("У вас есть", len(word), "попыток.")

    while True:
        print("Загаданное слово:", display_word(word, guessed_letters))
        guess = input("Введите букву: ").lower()

        if guess.startswith("!"):
            if guess == "!help":
                display_commands()
            elif guess == "!used":
                print("Использованные буквы:", ", ".join(guessed_letters))
            elif guess == "!remaining":
                print("Оставшиеся буквы:", ", ".join(remaining_latters))
            else:
                print("Неверная команда!")
            continue

        if not validate_input(guess):
            print("Неверный ввод!")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву!")
            continue

        guessed_letters.append(guess)
        remaining_latters.remove(guess)

        if guess in word:
            print("Вы угадали букву!")
        else:
            print("Такой буквы нет!")

        if all(letter in guessed_letters for letter in word):
            print("Вы победили! Загаданное слово:", word)
            print("Количество попыток:", attempts)
            break

        attempts += 1

    print("Спасибо за игру!")

# Запуск игры
play_game()
