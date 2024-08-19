# Матрица воплоти
def get_matrix(n = 1,m = 1, value = 1):
    matrix = []
    for tr in range(0,n):
        td = []
        for ii in range(0,m):
            td.append(value)
        matrix.insert(tr,td)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)