# Решение с numpy/scipy '''python
# Изготвил: Стилиян Игнатов ф.н 233010002
# Сравнение от метода  Крамер и numpy/linalg.solve in Phyton
import numpy as np

# Дефиниране на коефициентната матрица A и вектора B
A = np.array([[3, 4, 1], [2, 3, 0], [4, 3, -1]])
B = np.array([1, 0, -2])

# Решение с numpy.linalg.solve
solution_numpy = np.linalg.solve(A, B)


# Решение с метода на Крамер
def kramer_solution(A, B):
    det_A = np.linalg.det(A)  # Детерминанта на A
    if det_A == 0:
        raise ValueError("Матрицата A е сингулярна и няма уникално решение.")

    # Създаване на матриците Ax, Ay, Az
    A_x = A.copy()
    A_x[:, 0] = B  # Замяна на първата колона с B
    A_y = A.copy()
    A_y[:, 1] = B  # Замяна на втората колона с B
    A_z = A.copy()
    A_z[:, 2] = B  # Замяна на третата колона с B

    # Изчисляване на x, y, z
    x = np.linalg.det(A_x) / det_A
    y = np.linalg.det(A_y) / det_A
    z = np.linalg.det(A_z) / det_A

    return np.array([x, y, z])


solution_kramer = kramer_solution(A, B)

# Сравнение на резултатите
print("Решение с numpy.linalg.solve:")
print("x =", solution_numpy[0], ", y =", solution_numpy[1], ", z =", solution_numpy[2])

print("\nРешение с метода на Крамер:")
print("x =", solution_kramer[0], ", y =", solution_kramer[1], ", z =", solution_kramer[2])

# Проверка дали решенията съвпадат
are_equal = np.allclose(solution_numpy, solution_kramer)
print("\nСъвпадат ли решенията? ->", "Да" if are_equal else "Не")
