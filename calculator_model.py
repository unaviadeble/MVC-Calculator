class CalculatorModel:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0

    def add_numbers(self):
        self.result = self.num1 + self.num2

    def subtract_numbers(self):
        self.result = self.num1 - self.num2

    def multiply_numbers(self):
        self.result = self.num1 * self.num2

    def divide_numbers(self):
        if self.num2 != 0:
            self.result = self.num1 / self.num2
        else:
            self.result = "Ошибка: деление на ноль."

    def calculate_circle_area(self, radius):
        return 3.14 * radius * radius

    def calculate_rectangle_area(self, length, width):
        return length * width

    def calculate_triangle_area(self, base, height):
        return 0.5 * base * height
