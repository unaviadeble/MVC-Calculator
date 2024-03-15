from calculator_model import CalculatorModel
from calculator_view import CalculatorView
from calculator_controller import AreaCalculatorController, ClassicCalculatorController

model = CalculatorModel()
view = CalculatorView()
controller = ClassicCalculatorController(model, view)
AreaController = AreaCalculatorController(model, view)

while True:
    print("Выберите операцию:\n",
    "1. Сложение (+)\n",
    "2. Вычитание (-)\n",
    "3. Умножение (*)\n",
    "4. Деление (/)\n",
    "5. Площадь круга\n",
    "6. Площадь прямоугольника\n",
    "7. Площадь треугольника\n",
    "Введите 'q' для выхода.\n")

    choice = input("Ваш выбор: ")

    if choice == '1':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        controller.add_numbers(num1, num2)
    elif choice == '2':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        controller.subtract_numbers(num1, num2)
    elif choice == '3':
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        controller.multiply_numbers(num1, num2)
    elif choice == '4':
        num1 = float(input("Введите делимое: "))
        num2 = float(input("Введите делитель (не равный нулю): "))
        controller.divide_numbers(num1, num2)

    elif choice == '5':
        radius = float(input("Введите радиус круга: "))
        AreaController.calculate_circle_area(radius)
    elif choice == '6':
        length = float(input("Введите длину прямоугольника: "))
        width = float(input("Введите ширину прямоугольника: "))
        AreaController.calculate_rectangle_area(length, width)
    elif choice == '7':
        base = float(input("Введите основание треугольника: "))
        height = float(input("Введите высоту треугольника: "))
        AreaController.calculate_triangle_area(base, height)
    elif choice.lower() == 'q':
        break
    else:
        print("Некорректный ввод. Пожалуйста, попробуйте снова.")
