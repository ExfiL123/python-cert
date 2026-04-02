import math
from matrix import Matrix


class EquationSolver:
    """Класс для решения уравнений"""
    
    @staticmethod
    def solve_linear(a, b):
        """
        Решение линейного уравнения ax + b = 0
        :param a: коэффициент при x
        :param b: свободный член
        :return: решение уравнения
        """
        if a == 0:
            if b == 0:
                return "Бесконечно много решений"
            else:
                return "Нет решений"
        
        x = -b / a
        return f"x = {x:.4f}"
    
    @staticmethod
    def solve_quadratic(a, b, c):
        """
        Решение квадратного уравнения ax² + bx + c = 0
        :param a: коэффициент при x²
        :param b: коэффициент при x
        :param c: свободный член
        :return: решения уравнения
        """
        if a == 0:
            return EquationSolver.solve_linear(b, c)
        
        discriminant = b**2 - 4*a*c
        
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            return f"x₁ = {x1:.4f}, x₂ = {x2:.4f}"
        elif discriminant == 0:
            x = -b / (2*a)
            return f"x = {x:.4f} (один корень)"
        else:
            real_part = -b / (2*a)
            imag_part = math.sqrt(-discriminant) / (2*a)
            return f"x₁ = {real_part:.4f} + {imag_part:.4f}i, x₂ = {real_part:.4f} - {imag_part:.4f}i"
    
    @staticmethod
    def solve_system(coefficients, constants):
        """
        Решение системы линейных уравнений
        :param coefficients: матрица коэффициентов
        :param constants: вектор свободных членов
        :return: решение системы
        """
        # Создаем расширенную матрицу
        n = len(coefficients)
        augmented = []
        for i in range(n):
            row = coefficients[i] + [constants[i]]
            augmented.append(row)
        
        matrix = Matrix(augmented)
        
        try:
            solution = matrix.solve_gauss()
            result = []
            for i, x in enumerate(solution):
                result.append(f"x{i+1} = {x:.4f}")
            return ", ".join(result)
        except ValueError as e:
            return str(e)
