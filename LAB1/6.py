"""
Решение задачи о поиске минимального N-значного натурального числа
с заданной суммой цифр S.
"""

from typing import NoReturn


def find_minimal_number(n_digits: int, s_sum: int) -> str:
    """
    Находит минимальное N-значное натуральное число с суммой цифр S.

    Args:
        n_digits: Требуемое количество разрядов (N).
        s_sum: Требуемая сумма цифр (S).

    Returns:
        Строковое представление искомого числа или "NO", если такого числа нет.
    """
    # --- Проверка на невозможность ---
    # 1. Сумма не может быть больше, чем если бы все N цифр были девятками.
    # 2. По условию S >= 1. Если бы S=0 было возможно, то для N > 1 решения бы не было,
    #    а для N=1 число '0' не является натуральным.
    if s_sum > 9 * n_digits or s_sum < 1:
        return "NO"

    # --- Построение числа (жадный алгоритм) ---
    remaining_sum = s_sum
    result_digits = []

    # Итерируемся по каждой позиции цифры слева направо.
    for i in range(n_digits):
        is_first_digit = (i == 0)
        num_digits_left = n_digits - 1 - i

        # Определяем начальную цифру для перебора (1 для первой, 0 для остальных).
        start_digit = 1 if is_first_digit else 0

        # Находим наименьшую подходящую цифру для текущей позиции.
        for digit in range(start_digit, 10):
            # Проверяем, возможно ли составить оставшуюся сумму
            # (remaining_sum - digit) из оставшихся разрядов (num_digits_left).
            # Минимальная возможная сумма для оставшихся - 0.
            # Максимальная - 9 * num_digits_left.
            if 0 <= (remaining_sum - digit) <= 9 * num_digits_left:
                # Нашли самую маленькую подходящую цифру, ставим ее.
                result_digits.append(str(digit))
                remaining_sum -= digit
                break  # Переходим к следующей позиции.

    # Если после всех итераций длина результата не равна N, значит,
    # наше предположение о существовании решения было неверным.
    # (Хотя с текущей проверкой на невозможность это не должно произойти).
    if len(result_digits) == n_digits:
        return "".join(result_digits)
    else:
        return "NO"


def main() -> NoReturn:
    """
    Основная функция для считывания ввода и вывода результата.
    """
    try:
        n = int(input())
        s = int(input())

        result = find_minimal_number(n, s)
        print(result)

    except (ValueError, EOFError):
        # Обработка некорректного или пустого ввода.
        print("NO")


if __name__ == "__main__":
    main()