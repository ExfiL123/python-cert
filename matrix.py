from vector import Vector


class Matrix:
    """Класс для работы с матрицами"""
    
    def __init__(self, elements):
        """
        Инициализация матрицы
        :param elements: двумерный список элементов
        """
        if not elements or not elements[0]:
            raise ValueError("Матрица не может быть пустой")
        
        # Проверяем, что все строки одинаковой длины
        row_length = len(elements[0])
        for row in elements:
            if len(row) != row_length:
                raise ValueError("Все строки матрицы должны иметь одинаковую длину")
        
        self.elements = elements
        self.rows = len(elements)
        self.cols = len(elements[0])
    
    def add(self, other):
        """Сложение матриц"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковый размер")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.elements[i][j] + other.elements[i][j])
            result.append(row)
        
        return Matrix(result)
    
    def subtract(self, other):
        """Вычитание матриц"""
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны иметь одинаковый размер")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.elements[i][j] - other.elements[i][j])
            result.append(row)
        
        return Matrix(result)
    
    def multiply_vector(self, vector):
        """Умножение матрицы на вектор"""
        if self.cols != vector.dimension:
            raise ValueError("Количество столбцов матрицы должно совпадать с размерностью вектора")
        
        result = []
        for i in range(self.rows):
            value = sum(self.elements[i][j] * vector.coordinates[j] for j in range(self.cols))
            result.append(value)
        
        return Vector(result)
    
    def multiply(self, other):
        """Умножение матриц"""
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно равняться количеству строк второй")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                value = sum(self.elements[i][k] * other.elements[k][j] for k in range(self.cols))
                row.append(value)
            result.append(row)
        
        return Matrix(result)
    
    def transpose(self):
        """Транспонирование матрицы"""
        result = []
        for j in range(self.cols):
            row = []
            for i in range(self.rows):
                row.append(self.elements[i][j])
            result.append(row)
        
        return Matrix(result)
    
    def determinant(self):
        """Вычисление определителя квадратной матрицы"""
        if self.rows != self.cols:
            raise ValueError("Определитель можно вычислить только для квадратной матрицы")
        
        return self._det_recursive(self.elements)
    
    def _det_recursive(self, matrix):
        """Рекурсивное вычисление определителя"""
        n = len(matrix)
        
        if n == 1:
            return matrix[0][0]
        
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        det = 0
        for j in range(n):
            minor = self._get_minor(matrix, 0, j)
            det += ((-1) ** j) * matrix[0][j] * self._det_recursive(minor)
        
        return det
    
    def _get_minor(self, matrix, row, col):
        """Получение минора матрицы"""
        return [row[:col] + row[col+1:] for i, row in enumerate(matrix) if i != row]
    
    def solve_gauss(self):
        """
        Решение системы линейных уравнений методом Гаусса
        Матрица должна быть расширенной (A|b)
        """
        if self.rows + 1 != self.cols:
            raise ValueError("Для решения системы матрица должна быть расширенной (n x n+1)")
        
        # Создаем копию матрицы
        m = [row[:] for row in self.elements]
        n = self.rows
        
        # Прямой ход
        for i in range(n):
            # Поиск максимального элемента в столбце
            max_row = i
            for k in range(i + 1, n):
                if abs(m[k][i]) > abs(m[max_row][i]):
                    max_row = k
            
            m[i], m[max_row] = m[max_row], m[i]
            
            # Проверка на вырожденность
            if abs(m[i][i]) < 1e-10:
                raise ValueError("Система не имеет единственного решения")
            
            # Обнуление элементов под главной диагональю
            for k in range(i + 1, n):
                factor = m[k][i] / m[i][i]
                for j in range(i, n + 1):
                    m[k][j] -= factor * m[i][j]
        
        # Обратный ход
        solution = [0] * n
        for i in range(n - 1, -1, -1):
            solution[i] = m[i][n]
            for j in range(i + 1, n):
                solution[i] -= m[i][j] * solution[j]
            solution[i] /= m[i][i]
        
        return solution
    
    def __str__(self):
        """Строковое представление матрицы"""
        result = []
        for row in self.elements:
            result.append("[" + " ".join(f"{x:8.2f}" for x in row) + "]")
        return "\n".join(result)
