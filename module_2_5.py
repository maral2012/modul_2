
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
n = int(input('Введите число :'))
m = int(input('Введите число :'))
value = input(f'Введите число : ')
print('-------' * m)
matrix = get_matrix(n, m, value)