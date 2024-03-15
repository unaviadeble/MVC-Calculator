class ClassicCalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_numbers(self, num1, num2):
        result = self.model.add_numbers(num1, num2)
        self.view.display_result(result)

    def subtract_numbers(self, num1, num2):
        result = self.model.subtract_numbers(num1, num2)
        self.view.display_result(result)

    def multiply_numbers(self, num1, num2):
        result = self.model.multiply_numbers(num1, num2)
        self.view.display_result(result)

    def divide_numbers(self, num1, num2):
        result = self.model.divide_numbers(num1, num2)
        self.view.display_result(result)


class AreaCalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calculate_circle_area(self, radius):
        result = self.model.calculate_circle_area(radius)
        self.view.display_result(result)

    def calculate_rectangle_area(self, length, width):
        result = self.model.calculate_rectangle_area(length, width)
        self.view.display_result(result)

    def calculate_triangle_area(self, base, height):
        result = self.model.calculate_triangle_area(base, height)
        self.view.display_result(result)
