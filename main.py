from vector import Vector
from matrix import Matrix
from equation_solver import EquationSolver


def work_with_vectors():
    """Интерфейс для работы с векторами"""
    try:
        print("\n=== Работа с векторами ===")
        
        # Ввод первого вектора
        coords1 = input("Введите координаты первого вектора (через пробел): ").split()
        coords1 = [float(x) for x in coords1]
        v1 = Vector(coords1)
        
        print("\nВыберите операцию:")
        print("1. Длина вектора")
        print("2. Скалярное произведение")
        print("3. Угол между векторами")
        print("4. Сложение векторов")
        print("5. Вычитание векторов")
        print("6. Умножение на скаляр")
        print("7. Проверка коллинеарности")
        
        choice = input("Ваш выбор: ")
        
        if choice == '1':
            print(f"Длина вектора: {v1.length():.4f}")
        
        elif choice in ['2', '3', '4', '5', '7']:
            coords2 = input("Введите координаты второго вектора (через пробел): ").split()
            coords2 = [float(x) for x in coords2]
            v2 = Vector(coords2)
            
            if choice == '2':
                print(f"Скалярное произведение: {v1.dot_product(v2):.4f}")
            elif choice == '3':
                print(f"Угол между векторами: {v1.angle(v2):.4f}°")
            elif choice == '4':
                result = v1.add(v2)
                print(f"Сумма векторов: {result}")
            elif choice == '5':
                result = v1.subtract(v2)
                print(f"Разность векторов: {result}")
            elif choice == '7':
                if v1.is_collinear(v2):
                    print("Векторы коллинеарны")
                else:
                    print("Векторы не коллинеарны")
        
        elif choice == '6':
            scalar = float(input("Введите скаляр: "))
            result = v1.multiply_scalar(scalar)
            print(f"Результат: {result}")
        
        else:
            print("Неверный выбор")
    
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def work_with_matrices():
    """Интерфейс для работы с матрицами"""
    try:
        print("\n=== Работа с матрицами ===")
        
        # Ввод первой матрицы
        rows, cols = map(int, input("Введите размер первой матрицы (строки столбцы): ").split())
        print("Введите элементы первой матрицы (построчно):")
        elements1 = []
        for i in range(rows):
            row = list(map(float, input(f"Строка {i+1}: ").split()))
            if len(row) != cols:
                raise ValueError(f"Ожидалось {cols} элементов, получено {len(row)}")
            elements1.append(row)
        
        m1 = Matrix(elements1)
        
        print("\nВыберите операцию:")
        print("1. Сложение матриц")
        print("2. Вычитание матриц")
        print("3. Умножение матриц")
        print("4. Умножение матрицы на вектор")
        print("5. Транспонирование")
        print("6. Определитель")
        print("7. Решение системы уравнений (метод Гаусса)")
        
        choice = input("Ваш выбор: ")
        
        if choice in ['1', '2', '3']:
            print("Введите элементы второй матрицы:")
            if choice == '3':
                rows2 = cols
                cols2 = int(input(f"Количество столбцов второй матрицы: "))
            else:
                rows2, cols2 = rows, cols
            
            elements2 = []
            for i in range(rows2):
                row = list(map(float, input(f"Строка {i+1}: ").split()))
                if len(row) != cols2:
                    raise ValueError(f"Ожидалось {cols2} элементов")
                elements2.append(row)
            
            m2 = Matrix(elements2)
            
            if choice == '1':
                result = m1.add(m2)
                print("Результат сложения:")
                print(result)
            elif choice == '2':
                result = m1.subtract(m2)
                print("Результат вычитания:")
                print(result)
            elif choice == '3':
                result = m1.multiply(m2)
                print("Результат умножения:")
                print(result)
        
        elif choice == '4':
            coords = input(f"Введите координаты вектора ({cols} элементов через пробел): ").split()
            coords = [float(x) for x in coords]
            v = Vector(coords)
            result = m1.multiply_vector(v)
            print(f"Результат: {result}")
        
        elif choice == '5':
            result = m1.transpose()
            print("Транспонированная матрица:")
            print(result)
        
        elif choice == '6':
            det = m1.determinant()
            print(f"Определитель: {det:.4f}")
        
        elif choice == '7':
            if rows + 1 != cols:
                print("Для решения системы введите расширенную матрицу (n x n+1)")
            else:
                solution = m1.solve_gauss()
                print("Решение системы:")
                for i, x in enumerate(solution):
                    print(f"x{i+1} = {x:.4f}")
        
        else:
            print("Неверный выбор")
    
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def work_with_equations():
    """Интерфейс для работы с уравнениями"""
    try:
        print("\n=== Решение уравнений ===")
        print("Выберите тип уравнения:")
        print("1. Линейное (ax + b = 0)")
        print("2. Квадратное (ax² + bx + c = 0)")
        print("3. Система линейных уравнений")
        
        choice = input("Ваш выбор: ")
        
        if choice == '1':
            a = float(input("Введите коэффициент a: "))
            b = float(input("Введите коэффициент b: "))
            result = EquationSolver.solve_linear(a, b)
            print(f"Решение: {result}")
        
        elif choice == '2':
            a = float(input("Введите коэффициент a: "))
            b = float(input("Введите коэффициент b: "))
            c = float(input("Введите коэффициент c: "))
            result = EquationSolver.solve_quadratic(a, b, c)
            print(f"Решение: {result}")
        
        elif choice == '3':
            n = int(input("Введите количество уравнений: "))
            print("Введите коэффициенты системы:")
            coefficients = []
            for i in range(n):
                row = list(map(float, input(f"Уравнение {i+1} (коэффициенты через пробел): ").split()))
                if len(row) != n:
                    raise ValueError(f"Ожидалось {n} коэффициентов")
                coefficients.append(row)
            
            constants = list(map(float, input("Введите свободные члены (через пробел): ").split()))
            if len(constants) != n:
                raise ValueError(f"Ожидалось {n} свободных членов")
            
            result = EquationSolver.solve_system(coefficients, constants)
            print(f"Решение: {result}")
        
        else:
            print("Неверный выбор")
    
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def main():
    """Главная функция программы"""
    print("=" * 50)
    print("Математическая библиотека")
    print("=" * 50)
    
    while True:
        print("\nВыберите действие:")
        print("1. Работа с векторами")
        print("2. Работа с матрицами")
        print("3. Решение уравнений")
        print("0. Выход")
        
        choice = input("\nВаш выбор: ")
        
        if choice == '1':
            work_with_vectors()
        elif choice == '2':
            work_with_matrices()
        elif choice == '3':
            work_with_equations()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
