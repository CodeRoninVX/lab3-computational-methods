# Модель: Метод Ньютона (5 семестр)
# Автор: Ахмадзада Вахід, група АІ-232

def f(x):
    # Функція, корінь якої шукаємо: x^3 - 2x - 5
    return x**3 - 2*x - 5

def f_prime(x):
    # Похідна функції: 3x^2 - 2
    return 3*x**2 - 2

def newton_method(x0, tolerance=1e-6, max_iterations=100):
    """
    Метод Ньютона для знаходження кореня рівняння.
    x0 - початкове наближення
    tolerance - точність
    max_iterations - максимальна кількість ітерацій
    """
    x = x0
    for i in range(max_iterations):
        fx = f(x)
        fpx = f_prime(x)

        if abs(fpx) < 1e-12:
            print("Похідна близька до нуля, метод зупинено.")
            return None

        x_new = x - fx / fpx

        print(f"Ітерація {i+1}: x = {x_new:.8f}, f(x) = {f(x_new):.8f}")

        if abs(x_new - x) < tolerance:
            print(f"\nКорінь знайдено: x = {x_new:.8f}")
            print(f"Кількість ітерацій: {i+1}")
            return x_new

        x = x_new

    print("Метод не збігся за задану кількість ітерацій.")
    return None

# Запуск методу
print("=== Метод Ньютона ===")
print("Рівняння: x^3 - 2x - 5 = 0")
print()
result = newton_method(x0=2.0)