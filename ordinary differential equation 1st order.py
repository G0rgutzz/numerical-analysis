import sympy as sp

def solve_separated_equation():
    print("=== Solving differential equation with separated variables ===")
    print("Equation form: dy/dx = f(x) * g(y)\n")
    x = sp.symbols('x')
    y = sp.Function('y')(x)

# ===== 2. Equation definition dy/dx = g(x)*h(y) =====
    print("Write function f(x) (e.g.: x**2, sin(x), 1):")
    f_str = input("f(x) = ")
    print("Write function g(y) (e.g.: y, y**2, exp(y), 1):")
    g_str = input("g(y) = ")

    try:
        # Parsing function
        f = sp.sympify(f_str)
        g = sp.sympify(g_str)
        print(f"\nEquation: dy/dx = {f} * {g.subs('y', y)}")
        # Separating variables: dy / g(y) = f(x) dx
        left_side = 1 / g
        right_side = f

        print(f"\nSeparated: dy / {g} = {f} dx")

        # Integrating the left side with respect to y
        y_var = sp.symbols('y')
        left_integral = sp.integrate(left_side.subs('y', y_var), y_var)

        # Integrating the left side with respect to x
        right_integral = sp.integrate(right_side, x)

        # Equation after integrating
        equation = sp.Eq(left_integral, right_integral + sp.symbols('C'))

        print(f"\nAfter integrating:")
        sp.pprint(equation) # sp.pprint -> prettier form

        # Attempt at explicit solution y(x)
        print("\nAttempting explicit solution y(x)...")
        try:
            y_explicit = sp.solve(equation, y_var)
            if y_explicit:
                print("\nExplicit solution y(x):")
                for sol in y_explicit:
                    sp.pprint(sp.Eq(y, sol.subs(y_var, y)))
            else:
                print("Couldn't solve y(x) explicitly.")
        except:
            print("Can't solve explicitly with respect to y.")

        # Getting implicit solution
        print(f"\nGeneral solution (implicit):")
        sp.pprint(equation)

    except Exception as e:
        print(f"Error: {e}")
        print("Make sure your functions are written correctly (use ** for power, sin(x), exp(y) itp.)")

# Starting
solve_separated_equation()
