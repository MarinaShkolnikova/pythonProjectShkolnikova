import random

def fill_array(start, end, size):
    array = [random.randint(start, end) for _ in range(size)]
    return array

def main():
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))
    size = 10  # размер массива

    array = fill_array(start, end, size)

    print("Значения элементов массива:")
    for element in array:
        print(element)

main()