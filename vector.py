import math


class Vector:
    """Класс для работы с векторами"""
    
    def __init__(self, coordinates):
        """
        Инициализация вектора
        :param coordinates: список координат вектора
        """
        if not coordinates:
            raise ValueError("Вектор не может быть пустым")
        self.coordinates = coordinates
        self.dimension = len(coordinates)
    
    def length(self):
        """Вычисляет длину вектора"""
        return math.sqrt(sum(x**2 for x in self.coordinates))
    
    def dot_product(self, other):
        """
        Скалярное произведение двух векторов
        :param other: другой вектор
        :return: скалярное произведение
        """
        if self.dimension != other.dimension:
            raise ValueError("Векторы должны иметь одинаковую размерность")
        return sum(a * b for a, b in zip(self.coordinates, other.coordinates))
    
    def angle(self, other):
        """
        Угол между двумя векторами в градусах
        :param other: другой вектор
        :return: угол в градусах
        """
        if self.dimension != other.dimension:
            raise ValueError("Векторы должны иметь одинаковую размерность")
        
        dot = self.dot_product(other)
        len1 = self.length()
        len2 = other.length()
        
        if len1 == 0 or len2 == 0:
            raise ValueError("Нулевой вектор не имеет направления")
        
        cos_angle = dot / (len1 * len2)
        # Ограничиваем значение из-за погрешностей вычислений
        cos_angle = max(-1, min(1, cos_angle))
        return math.degrees(math.acos(cos_angle))
    
    def add(self, other):
        """
        Сложение векторов
        :param other: другой вектор
        :return: новый вектор - сумма
        """
        if self.dimension != other.dimension:
            raise ValueError("Векторы должны иметь одинаковую размерность")
        result = [a + b for a, b in zip(self.coordinates, other.coordinates)]
        return Vector(result)
    
    def subtract(self, other):
        """
        Вычитание векторов
        :param other: другой вектор
        :return: новый вектор - разность
        """
        if self.dimension != other.dimension:
            raise ValueError("Векторы должны иметь одинаковую размерность")
        result = [a - b for a, b in zip(self.coordinates, other.coordinates)]
        return Vector(result)
    
    def multiply_scalar(self, scalar):
        """
        Умножение вектора на скаляр
        :param scalar: число
        :return: новый вектор
        """
        result = [x * scalar for x in self.coordinates]
        return Vector(result)
    
    def is_collinear(self, other):
        """
        Проверка коллинеарности векторов
        :param other: другой вектор
        :return: True если векторы коллинеарны
        """
        if self.dimension != other.dimension:
            return False
        
        # Находим первую ненулевую координату
        ratio = None
        for a, b in zip(self.coordinates, other.coordinates):
            if a == 0 and b == 0:
                continue
            if a == 0 or b == 0:
                return False
            current_ratio = a / b
            if ratio is None:
                ratio = current_ratio
            elif abs(ratio - current_ratio) > 1e-10:
                return False
        
        return True
    
    def __str__(self):
        """Строковое представление вектора"""
        return f"({', '.join(map(str, self.coordinates))})"
