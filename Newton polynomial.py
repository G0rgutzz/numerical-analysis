import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def newton_divided_diff(x, y):
    """
    Oblicza tablicę różnic dzielonych dla danych (x, y)
    """
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j - 1]) / (x[j:n] - x[j - 1])
    return coef

def newton_polynomial(x_data, coef):
    """
    Zwraca symboliczny wielomian interpolacyjny Newtona
    """
    x = sp.Symbol('x')
    n = len(coef)
    polynomial = 0
    for i in range(n):
        term = coef[i]
        for j in range(i):
            term *= (x - x_data[j])
        polynomial += term
    return sp.expand(polynomial)

def newton_interpolate(x_data, y_data, x_value):
    """
    Oblicza wartość interpolacji Newtona w punkcie x_value
    """
    coef = newton_divided_diff(x_data, y_data)
    n = len(coef)
    result = coef[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x_value - x_data[i]) + coef[i]
    return result

# ===== PRZYKŁAD UŻYCIA =====
if __name__ == "__main__":
    # Punkty danych
    x_points = np.array([1, 2, 3, 4])
    y_points = np.array([1, 4, 9, 16])  # funkcja f(x) = x^2

    # Obliczenie współczynników i wielomianu symbolicznego
    coef = newton_divided_diff(x_points, y_points)
    poly = newton_polynomial(x_points, coef)

    print("Różnice dzielone (współczynniki):", coef)
    print("Wielomian Newtona:")
    print(poly)

    # Obliczenie wartości interpolacji
    x_val = 2.5
    y_val = newton_interpolate(x_points, y_points, x_val)
    print(f"\nInterpolacja w punkcie x={x_val}: y={y_val}")

    # (opcjonalnie) rysunek
    X = np.linspace(min(x_points), max(x_points), 100)
    Y = [newton_interpolate(x_points, y_points, xx) for xx in X]
    plt.scatter(x_points, y_points, color='red', label='Punkty dane')
    plt.plot(X, Y, label='Wielomian Newtona')
    plt.title("Interpolacja Newtona")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
