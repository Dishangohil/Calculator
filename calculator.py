# calculator.py

def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            return num1 / num2 if num2 != 0 else 'Cannot divide by zero'
        else:
            return 'Invalid operation'
    except ValueError:
        return 'Invalid input'
