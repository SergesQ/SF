message = "Введите последовательность целых чисел через пробел:\n"

array = input(message)


while array.replace(" ", "").isdigit() != True:
    print("Введены недопустимые символы.\nИспользуйте только целые числа и пробел")
    array = input(message)

array = list(map(int, array.split(' ')))
def sorting(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:
            array[i], array[idx_min] = array[idx_min], array[i]

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return f"Ваше число имеет индекс {middle}"
    elif element < array[middle]:
        if left == right or left == middle:
            return f"Ваше число имеет индекс {middle}"
        return binary_search(array, element, left, middle - 1)
    elif element >= array[middle]:
        if left == right:
            return f"Ваше число имеет индекс {middle + 1}"
        return binary_search(array, element, middle + 1, right)

sorting(array)
print(f'Ваш список, отсортированный по возрастанию: {array}')
element = input('Введите целое число: ')
while element.isdigit() != True:
    element = input("Ошибка ввода. Введите целое число: ")
element = int(element)
print(binary_search(array, element, 0, len(array ) -1))
