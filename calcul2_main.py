import logging

logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='[Line %(lineno)d] %(message)s'
)

def calcul_main_example(example: str) -> float:
    
    """
    Примеры использования:
        >>> calcul_main_example('+ 5 5')
        25.0
        >>> calcul_main_example('- 9 4')
        5.0
    """
    try:
        # Делим строку на части
        parts = example.strip().split()
        if len(parts) != 3:
            raise ValueError("Неверный формат строки. Ожидается: 'операция число1 число2'.")

        operation, num1, num2 = parts
        num1, num2 = float(num1), float(num2)

        # Выполняем операцию
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            return num1 / num2
        else:
            raise ValueError(f"Недопустимая операция '{operation}'. Допустимые операции: +, -, *, /.")

    except ValueError as ve:
        raise ValueError(f"Ошибка при обработке строки '{example}': {ve}")
    except ZeroDivisionError as zde:
        raise ZeroDivisionError(f"Ошибка при обработке строки '{example}': {zde}")


def process_file(file_path: str) -> None:
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                example = line.strip()
                if not example:
                    continue  # Пропускаем пустые строки

                try:
                    result = calcul_main_example(example)
                    print(f"Результат выражения '{example}' (строка {line_number}): {result}")
                except (ValueError, ZeroDivisionError) as e:
                    # Логируем ошибку в файл
                    logging.error(f"[Строка {line_number}] {e}")
                    # Выводим ошибку в консоль
                    print(f"Ошибка в выражении '{example}' (строка {line_number}): {e}")

    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")



if __name__ == "__main__":
   
    file_path = 'text.txt'
    process_file(file_path)