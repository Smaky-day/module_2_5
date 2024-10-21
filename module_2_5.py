def get_matrix(n, m, value):
    matrix = []  # пустой список
    for i in range(n):   # внешн. цикл для повторов n
        empty_list = []  # добавим пустой список в matrix
        matrix.append(empty_list)  # пропишем что его значения будут внесены в matrix
        for j in range(m):   # внутр. цикл для столбцов m повторов
            empty_list.append(value)  # пополнима список empty_list значениями value
    return matrix   # вернем значение первого пустого списка
result1 = get_matrix(2, 2, 10)
print(result1)
result1 = get_matrix(1, 3, 13)
print(result1)
result1 = get_matrix(7, 7, 7)
print(result1)
result1 = get_matrix(2, 3, 4)
print(result1)