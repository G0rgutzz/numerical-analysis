import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# ===== Function definition =====
x, y = sp.symbols('x y', real=True)

# Function example:
f = x ** 2 + y ** 2 + 3*x*x*y


# ===== 1. Partial derivatives =====
fx = sp.diff(f, x)
fy = sp.diff(f, y)

# ===== 2. Critical points =====
critical_points = sp.solve([fx, fy], (x, y), dict=True)

print("Punkty krytyczne:")
for p in critical_points:
    print(p)

# ===== 3. Test of second derivatives (Hesse's matrix) =====
fxx = sp.diff(fx, x)
fyy = sp.diff(fy, y)
fxy = sp.diff(fx, y)

print("\nAnaliza drugich pochodnych:")
print(f"fxx = {fxx}")
print(f"fyy = {fyy}")
print(f"fxy = {fxy}")


def classify_point(px, py):
    """Klasyfikacja punktu krytycznego metodą Hessego"""
    D = fxx.subs({x: px, y: py}) * fyy.subs({x: px, y: py}) - fxy.subs({x: px, y: py}) ** 2
    fxx_val = fxx.subs({x: px, y: py})
    f_val = f.subs({x: px, y: py})

    if D > 0:
        if fxx_val > 0:
            type = "minimum lokalne"
        else:
            type = "maksimum lokalne"
    elif D < 0:
        type = "punkt siodłowy"
    else:
        type = "nieokreślony"

    return type, float(f_val)


def visualisation():
    # ===== 4. (Optional) 3D visualisation =====
    #grid coordinates
    X = np.linspace(-5, 5, 40)
    Y = np.linspace(-5, 5, 40)
    X, Y = np.meshgrid(X, Y)
    Z = sp.lambdify((x, y), f, "numpy")(X, Y)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

    # marking critical points
    for px, py, f_val, typ in classified_points:
        color = {'minimum lokalne': 'red', 'maksimum lokalne': 'blue', 'punkt siodłowy': 'black'}.get(typ, 'gray')
        ax.scatter(px, py, f_val, color=color, s=60, label=typ)

    ax.set_title("Ekstrema funkcji dwóch zmiennych")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")
    plt.legend()
    plt.show()


print("\nKlasyfikacja punktów:")
classified_points = []
for p in critical_points:
    px, py = p[x], p[y]
    typ, f_val = classify_point(px, py)
    classified_points.append((float(px), float(py), f_val, typ))
    print(f"Punkt ({px}, {py}) -> {typ}, f = {f_val}")
visualisation()
