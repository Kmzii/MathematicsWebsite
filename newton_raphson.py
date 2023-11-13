import sympy as sp


def calculate_root(function_str, initial_guess, iterations):
    x = sp.symbols('x')

    try:
        function = sp.sympify(function_str)
        derivative = sp.diff(function, x)

        # Validate the initial guess
        try:
            guess = float(initial_guess)  # Convert guess to float
        except ValueError:
            raise ValueError("Invalid initial guess. Please enter a valid float number.")

        results = []

        for _ in range(iterations):
            try:
                func_value = function.subs(x, guess)
                der_value = derivative.subs(x, guess)

                if der_value == 0:
                    break  # To prevent division by zero

                guess = guess - func_value / der_value
                results.append(guess)
            except ZeroDivisionError:
                break  # To prevent division by zero

        return results

    except (ValueError, sp.SympifyError) as ve:
        raise ValueError("Invalid input. Check your function or initial guess.")
    except Exception as e:
        raise ValueError("Error in Newton-Raphson iteration: " + str(e))
