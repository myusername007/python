import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# -----------------------
# Дані (варіант 9 — X8, Y8)
# -----------------------
X = np.array([6.15, 5.66, 7.50, 6.90, 8.31, 8.25, 9.39, 9.73, 9.33,
              10.50, 11.10, 11.51, 12.42, 12.40, 13.14])

Y = np.array([19.66, 20.53, 21.31, 22.59, 23.27, 24.44, 25.85, 26.74,
              27.36, 28.37, 29.22, 30.50, 31.21, 32.56, 33.66])

# -----------------------
# 1. Лінійна регресія
# -----------------------
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)

print("Рівняння регресії:  Y = a + bX")
print(f"a (intercept) = {intercept}")
print(f"b (slope)     = {slope}")

# -----------------------
# 2. Коефіцієнт детермінації
# -----------------------
R2 = r_value**2
print("Коефіцієнт детермінації R^2 =", R2)

# -----------------------
# 3. Кореляція Пірсона
# -----------------------
print("Кореляція Пірсона r =", r_value)

# -----------------------
# 4. Графік регресії
# -----------------------
plt.figure(figsize=(7,5))
plt.scatter(X, Y, color='blue', label='Емпіричні дані')
plt.plot(X, intercept + slope*X, color='red', label='Регресійна пряма')
plt.xlabel("X (фактор)")
plt.ylabel("Y (результат)")
plt.title("Лінійна регресія Y залежно від X")
plt.grid(True)
plt.legend()
plt.show()
