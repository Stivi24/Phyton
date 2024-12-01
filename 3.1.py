# Решение с numpy/scipy '''python'''
# Изготвил: Стилиян Игнатов ф.н 233010002

import numpy as np

# Матрица C
C = np.array([[3, 0, 1], [2, -1, 0], [-4, 2, -4]])
det_C = np.linalg.det(C)
print("Детерминанта на C:", det_C)

# Матрица D
D = np.array([[3, 0, 1], [0, -1, 0], [1, 0, -3]])
eigenvalues, _ = np.linalg.eig(D)
print("Собствени стойности на D:", eigenvalues)

# Ръчно изчислени стойности
manual_det_C = 12
manual_eigenvalues_D = [3, -1, -3]

# Сравнение на детерминанти
is_det_C_correct = np.isclose(det_C, manual_det_C)
print("\nСъвпада ли детерминантата на C? ->", "Да" if is_det_C_correct else "Не")

# Сравнение на собствени стойности
is_eigenvalues_correct = np.allclose(sorted(eigenvalues), sorted(manual_eigenvalues_D))
print("Съвпадат ли собствените стойности на D? ->", "Да" if is_eigenvalues_correct else "Не")
