from collections import deque


# Задание 1
def sort_book_titles():
    # Чтение строк из файла
    with open('book.txt', 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file]

        # Используем два дека для сортировки строк в алфавитном порядке
        original_deque = deque(sorted(lines))
        sorted_deque = deque()

        # Переносим строки из отсортированного дека в результирующий дек
        while original_deque:
            sorted_deque.append(original_deque.pop())

    # Записываем отсортированные строки обратно в файл
    with open('sorted_book.txt', 'w', encoding='utf-8') as file:
        while sorted_deque:
            file.write(sorted_deque.pop() + '\n')


# Вызываем функцию для сортировки строк в файле
sort_book_titles()


# Задание 2
def deshifr(ciphertext, deck):
    decrypted_text = ''

    for char in ciphertext:
        if char.isalpha():  # Обрабатываем только буквы
            if deck.index(char) - 2 < 0:
                decrypted_char = deck[deck.index(char) - 2 + 26]
                decrypted_text += decrypted_char
            elif 0 < deck.index(char) - 2 < 26:
                decrypted_char = deck[deck.index(char) - 2]
                decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text


# Создаем дек с символами, которые использовались для шифровки
deck = deque("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Пример использования с зашифрованным сообщением
with open('зашифрованное.txt', 'r', encoding='utf-8') as file:
    with open('расшифрованное.txt', 'a', encoding='utf-8') as output_file:
        for line in file:
            decrypted_line = deshifr(line.strip().upper(), deck)
            output_file.write(decrypted_line + '\n')


# Зашифровать слово
def shifr(w):
    sh_word = ''

    for char in w:
        if char.isalpha():  # Обрабатываем только буквы
            if deck.index(char) + 2 > 0:
                sh_char = deck[deck.index(char) + 2 - 26]
                sh_word += sh_char
            elif 0 < deck.index(char) + 2 < 26:
                sh_char = deck[deck.index(char) + 2]
                sh_word += sh_char
        else:
            sh_word += char

    return sh_word


# print(shifr('I love Python'.upper()))


# Задание 3
print('____________________________________')
print('Задание 3')


def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from peg source({source}) to peg destination({destination})")
        destination.append(source.pop())
        print(source, destination, auxiliary)
        return

    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from peg source({source}) to peg destination({destination})")
    destination.append(source.pop())
    print(source, destination, auxiliary)
    tower_of_hanoi(n - 1, auxiliary, destination, source)


# Чтение данных из файла
with open('данные_о_дисках.txt', 'r', encoding='utf-8') as file:
    disks = [int(line.strip()) for line in file]

# Инициализация стеков
stack_a = list(disks)
stack_b = []
stack_c = []
print("Стек A:", stack_a)
print("Стек B:", stack_b)
print("Стек C:", stack_c)

# Вызов функции алгоритма Ханой
tower_of_hanoi(len(disks), stack_a, stack_c, stack_b)

# Вывод результатов
print("Стек A:", stack_a)
print("Стек B:", stack_b)
print("Стек C:", stack_c)

# Задание 4
print('____________________________________')
print('Задание 4')


def check_bracket_balance():
    stack = []
    open_brackets = {'(', '{', '['}
    close_brackets = {')': '(', '}': '{', ']': '['}

    with open('program_file.txt', 'r') as file:
        for line_num, line in enumerate(file, start=1):
            for char_num, char in enumerate(line, start=1):
                if char in open_brackets:
                    stack.append((char, line_num, char_num))
                elif char in close_brackets:
                    if not stack or stack[-1][0] != close_brackets[char]:
                        print(f"Ошибка: Лишняя закрывающая скобка '{char}' в строке {line_num}, позиция {char_num}")
                        return
                    stack.pop()

    for bracket, line_num, char_num in stack:
        print(f"Ошибка: Лишняя открывающая скобка '{bracket}' в строке {line_num}, позиция {char_num}")

    if not stack:
        print("Баланс скобок соблюден.")
    else:
        print("Ошибка: Остались несогласованные открывающие скобки.")


check_bracket_balance()

# Задание 5
print('____________________________________')
print('Задание 5')


def check_square_bracket_balance():
    stack = deque()

    with open('program_file2.txt', 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            for char_num, char in enumerate(line, start=1):
                if char == '[':
                    stack.append(('[', line_num, char_num))
                elif char == ']':
                    if not stack or stack[-1][0] != '[':
                        print(
                            f"Ошибка: Лишняя закрывающая квадратная скобка ']' в строке {line_num}, позиция {char_num}")
                        return
                    stack.pop()

    for bracket, line_num, char_num in stack:
        print(
            f"Ошибка: Лишняя открывающая квадратная скобка '{bracket}' в строке {line_num}, позиция {char_num}")

    if not stack:
        print("Баланс квадратных скобок соблюден.")
    else:
        print("Ошибка: Остались лишние открывающие квадратные скобки.")


check_square_bracket_balance()

# Задание 6
print('____________________________________')
print('Задание 6')


def print_characters_in_groups():
    digits_stack = []
    letters_stack = []
    other_stack = []

    with open('file_example6.txt', 'r') as file:
        for line in file:
            for char in line:
                if char.isdigit():
                    digits_stack.append(char)
                elif char.isalpha():
                    letters_stack.append(char)
                else:
                    other_stack.append(char)

    # Печать цифр
    print("Цифры:", *digits_stack, end=" ")
    print()

    # Печать букв
    print("Буквы:", *letters_stack, end=" ")
    print()

    # Печать остальных символов
    print("Остальные символы:", str(other_stack), end=" ")
    print()


print_characters_in_groups()

# Задание 7
print('____________________________________')
print('Задание 7')


def print_numbers_in_groups():
    negative_numbers = deque()
    positive_numbers = deque()

    with open('example_numbers7.txt', 'r') as file:
        for line in file:
            numbers = [int(num) for num in line.split()]
            for num in numbers:
                if num < 0:
                    negative_numbers.append(num)
                else:
                    positive_numbers.append(num)

    # Печать отрицательных чисел
    print("Отрицательные числа:", end=" ")
    while negative_numbers:
        print(negative_numbers.popleft(), end=" ")
    print()

    # Печать положительных чисел
    print("Положительные числа:", end=" ")
    while positive_numbers:
        print(positive_numbers.popleft(), end=" ")
    print()


# Пример использования
print_numbers_in_groups()


# Задание 8
def reverse_file_content():
    stack = []

    # Чтение строк из исходного файла и добавление их в стек
    with open('file_example8.txt', 'r') as file:
        for line in file:
            stack.append(line.strip())

    # Запись строк из стека в обратном порядке в новый файл
    with open('output_file_example8.txt', 'w') as output_file:
        while stack:
            output_file.write(stack.pop() + '\n')


reverse_file_content()
