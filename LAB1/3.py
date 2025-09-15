"""
Это решение вычисляет время окончания чистки зубов, основываясь на
количестве зубов и времени, затрачиваемом на чистку одного зуба.
"""

from typing import Tuple

# Константы для улучшения читаемости и упрощения изменений в будущем.
START_HOUR: int = 8
MINUTES_IN_HOUR: int = 60
NUM_ROWS_OF_TEETH: int = 2


def calculate_brushing_finish_time(
    teeth_per_row: int,
    minutes_per_tooth: int
) -> Tuple[int, int]:
    """
    Рассчитывает итоговое время на часах после чистки всех зубов.

    Аргументы:
        teeth_per_row (int): Количество зубов в одном ряду (X).
        minutes_per_tooth (int): Количество минут на чистку одного зуба (Y).

    Возвращает:
        Tuple[int, int]: Кортеж, содержащий итоговые час и минуту.
    """
    # 1. Вычисляем общее количество зубов.
    total_teeth = teeth_per_row * NUM_ROWS_OF_TEETH

    # 2. Вычисляем общее время чистки в минутах.
    total_brushing_duration_minutes = total_teeth * minutes_per_tooth

    # 3. Переводим время начала (8:00) в минуты от полуночи для удобства расчетов.
    start_time_in_minutes = START_HOUR * MINUTES_IN_HOUR

    # 4. Находим время окончания в минутах от полуночи.
    finish_time_in_minutes = start_time_in_minutes + total_brushing_duration_minutes

    # 5. Конвертируем итоговое время обратно в формат "часы и минуты".
    #    Используем целочисленное деление для часов и остаток от деления для минут.
    final_hour = finish_time_in_minutes // MINUTES_IN_HOUR
    final_minute = finish_time_in_minutes % MINUTES_IN_HOUR

    return final_hour, final_minute


def main() -> None:
    """
    Основная функция программы: считывает входные данные, вызывает функцию
    для расчета времени и выводит результат в требуемом формате.
    """
    try:
        # Считываем входные данные, как указано в условии.
        x = int(input())  # Количество зубов в ряду
        y = int(input())  # Минут на один зуб

        # Вызываем функцию для выполнения расчетов.
        finish_hour, finish_minute = calculate_brushing_finish_time(x, y)

        # Выводим результат: часы и минуты на отдельных строках.
        print(finish_hour)
        print(finish_minute)

    except (ValueError, EOFError):
        # Обработка возможных ошибок ввода, хотя по условию задачи
        # ввод всегда корректен.
        print("Ошибка: Введите два целых числа.")


if __name__ == "__main__":
    main()