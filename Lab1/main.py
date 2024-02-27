from time import time
from copy import deepcopy
from random import randint

# 1 задание
print('Hello, World')

# 2 задание
m, n, min_lim, max_lim = [int(input()) for _ in range(4)]

matrix = [[randint(0, 100) for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = randint(min_lim, max_lim)


# 3 задание
def selection_sort(matrix):
    """
    Сортировка строк матрицы методом выбора.
    """
    for i in range(len(matrix)):
        min_idx = i
        for j in range(i + 1, len(matrix)):
            if matrix[j][0] < matrix[min_idx][0]:
                min_idx = j
        matrix[i], matrix[min_idx] = matrix[min_idx], matrix[i]


def insertion_sort(matrix):
    """
    Сортировка строк матрицы методом вставки.
    """
    for i in range(len(matrix)):
        for j in range(1, len(matrix[i])):
            key = matrix[i][j]
            k = j - 1
            while k >= 0 and matrix[i][k] > key:
                matrix[i][k + 1] = matrix[i][k]
                k -= 1
            matrix[i][k + 1] = key


def bubble_sort(matrix):
    """
    Сортировка строк матрицы методом пузырька.
    """
    for i in range(len(matrix) - 1):
        for j in range(len(matrix) - i - 1):
            if matrix[j][0] > matrix[j + 1][0]:
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]


def shell_sort(matrix):
    """
    Сортировка строк матрицы методом Шелла.
    """
    gap = len(matrix) // 2
    while gap > 0:
        for i in range(gap, len(matrix)):
            for j in range(i - gap, -1, -gap):
                if matrix[j][0] > matrix[j + gap][0]:
                    matrix[j], matrix[j + gap] = matrix[j + gap], matrix[j]
        gap //= 2


def quicksort(matrix, low, high):
    """
    Сортировка строк матрицы методом быстрой сортировки.
    """
    if low < high:
        pi = partition(matrix, low, high)
        quicksort(matrix, low, pi - 1)
        quicksort(matrix, pi + 1, high)


def partition(matrix, low, high):
    """
    Разбиение матрицы на две части.
    """
    pivot = matrix[high][0]
    i = low - 1
    for j in range(low, high):
        if matrix[j][0] <= pivot:
            i += 1
            matrix[i], matrix[j] = matrix[j], matrix[i]
    matrix[i + 1], matrix[high] = matrix[high], matrix[i + 1]
    return i + 1


def tournament_sort(matrix):
    """
    Сортировка строк матрицы методом турнирной сортировки.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(n - 2 * i - 1):
            if matrix[j] < matrix[j + 1]:
                matrix[j], matrix[j + 1] = matrix[j + 1], matrix[j]

    return matrix


matrix_copy = deepcopy(matrix)
start_time = time()
matrix_copy.sort()
print("Время сортировки с помощью стандартной функции:", "--- {0} ms ---".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
selection_sort(matrix_copy)
print("Время сортировки методом выбора:", "--- {0} ms ---".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
insertion_sort(matrix_copy)
print("Время сортировки методом вставки:", "--- {0} ms ---".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
bubble_sort(matrix_copy)
print("Время сортировки методом пузырька:", "--- {0} ms ---".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
shell_sort(matrix_copy)
print("Время сортировки методом Шелла:", "--- {0} ms ---".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
quicksort(matrix_copy, 0, len(matrix_copy)-1)
print("Время сортировки методом быстрой сортировки:", "--- {0} ms ---".format(round((time() - start_time) * 1000)))

matrix_copy = deepcopy(matrix)
start_time = time()
tournament_sort(matrix_copy)
print("Время сортировки методом турнирной сортировки:", "--- {0} ms ---".format(round((time() - start_time) * 1000)))
