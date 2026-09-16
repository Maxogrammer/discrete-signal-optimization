#!/usr/bin/env python3
"""
Воспроизведение результатов эмпирического исследования статьи:
"Оптимальный период передачи дискретного сигнала между двумя системами"
Автор: Тубольцев М. Е. (2025)

Скрипт загружает 27-дневную телеметрию смартфонов (Data/PreparedExp/Phone1.json),
вычисляет оптимальные интервалы дискретизации tau по алгоритмам ЦНОД (CGCF)
и ММСП (MMSE), а затем рассчитывает погрешности и добротность zeta.
"""

import json
import sys
from pathlib import Path

# Определение путей относительно корня проекта
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "Data" / "PreparedExp" / "Phone1.json"
PAPER_PDF_PATH = BASE_DIR / "paper" / "optimal_discrete_signal_transmission.pdf"

# Сопоставление кодовых символов с типами активности (Раздел 4 статьи)
ACTIONS = {
    'O': 'Ожидание',
    '&': 'Видео',
    '@': 'Музыка',
    'I': 'Звонок'
}


def prime_divisors(n: int) -> list:
    """Нахождение уникальных простых делителей числа."""
    i = 2
    factors = set()
    d = n
    while i * i <= d:
        if d % i == 0:
            factors.add(i)
            d //= i
        else:
            i += 1
    if d > 1:
        factors.add(d)
    return list(factors)


def calc_tau_cnod(numbers: list) -> float:
    """
    Алгоритм ЦНОД (Центрированный наибольший общий делитель).
    Формула (16) статьи: tau = sum(l_i * p_i) / sum(l_j) (аналог центра масс).
    """
    freq = {}
    total_count = 0
    for num in numbers:
        divs = prime_divisors(num)
        for p in divs:
            freq[p] = freq.get(p, 0) + 1
            total_count += 1
    
    if total_count == 0:
        return 1.0
    
    weighted_sum = sum(p * count for p, count in freq.items())
    return round(weighted_sum / total_count, 3)


def calc_tau_mmsp(numbers: list, mode: str = "classic") -> float:
    """
    Алгоритм ММСП (Метод минимизации суммы погрешностей).
    Формула (14) статьи: одномерный сеточный поиск минимума суммарного отклонения.
    mode='classic': верхняя граница min(T) (Раздел 4)
    mode='modified': верхняя граница t_ср (Раздел 5)
    """
    if not numbers:
        return 1.0

    min_t = min(numbers)
    mean_t = sum(numbers) / len(numbers)
    upper_bound = min_t if mode == "classic" else mean_t

    delta_tau = 0.001
    tau = 1.0 + delta_tau
    best_tau = 1.0
    best_loss = sum(numbers)

    while tau <= upper_bound:
        loss = abs(sum(t - round(t / tau) * tau for t in numbers))
        if loss <= best_loss:
            best_loss = loss
            best_tau = tau
        tau += delta_tau

    return round(best_tau, 3)


def evaluate_telemetry(full_data: list, tau_dict: dict):
    """Расчет дифференциальной, интегральной погрешностей и добротности zeta."""
    diff_errors = []
    int_errors = []
    goodness_by_action = {k: [] for k in ACTIONS}

    for cycle in full_data:
        events = cycle[1:]
        cycle_total_time = 0
        cycle_abs_error = 0

        for duration, action in events:
            tau = tau_dict[action]
            step_count = round(duration / tau)
            abs_delta = abs(duration - step_count * tau)

            # Дифференциальная погрешность
            diff_errors.append(abs_delta / duration if duration > 0 else 0)

            # Добротность zeta = (|Delta t| / tau) * 100% (Формула 17)
            goodness_by_action[action].append((abs_delta / tau) * 100)

            cycle_abs_error += abs_delta
            cycle_total_time += duration

        # Интегральная погрешность цикла
        if cycle_total_time > 0:
            int_errors.append(cycle_abs_error / cycle_total_time)

    avg_diff = (sum(diff_errors) / len(diff_errors)) * 100 if diff_errors else 0
    avg_int = (sum(int_errors) / len(int_errors)) * 100 if int_errors else 0
    avg_goodness = {k: (sum(v) / len(v)) if v else 0 for k, v in goodness_by_action.items()}

    return avg_diff, avg_int, avg_goodness


def main():
    print("Экспериментальный бенчмарк алгоритмов дискретизации сигнала (ММСП / ЦНОД)")

    if not DATA_PATH.exists():
        print(f"Файл данных не найден по пути: {DATA_PATH}")
        sys.exit(1)

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        full_data = json.load(f)

    # Извлечение интервалов по типам активности
    action_durations = {k: [] for k in ACTIONS}
    for cycle in full_data:
        for duration, action in cycle[1:]:
            if action in action_durations:
                action_durations[action].append(duration)

    print(f"\nЗагружено 27 циклов телеметрии. Общее число событий: {sum(len(v) for v in action_durations.values())}")
    if PAPER_PDF_PATH.exists():
        print(f"[PDF] Текст статьи доступен: paper/{PAPER_PDF_PATH.name}")

    # Расчет tau
    tau_cnod = {k: calc_tau_cnod(v) for k, v in action_durations.items()}
    tau_mmsp_classic = {k: calc_tau_mmsp(v, mode="classic") for k, v in action_durations.items()}
    tau_mmsp_mod = {k: calc_tau_mmsp(v, mode="modified") for k, v in action_durations.items()}

    # Оценка качества
    diff_cnod, int_cnod, g_cnod = evaluate_telemetry(full_data, tau_cnod)
    diff_mmsp_c, int_mmsp_c, g_mmsp_c = evaluate_telemetry(full_data, tau_mmsp_classic)
    diff_mmsp_m, int_mmsp_m, g_mmsp_m = evaluate_telemetry(full_data, tau_mmsp_mod)

    # Вывод таблицы результатов (соответствует Разделам 4 и 5 статьи)
    print("\n" + "-" * 78)
    print(f"{'Режим':<12} | {'tau (ЦНОД)':<12} | {'tau (ММСП баз)':<15} | {'tau (ММСП мод)':<15} | {'zeta (ЦНОД)':<10}")
    print("-" * 78)
    for act, name in ACTIONS.items():
        print(f"{name:<12} | {tau_cnod[act]:<12.1f} | {tau_mmsp_classic[act]:<15.1f} | {tau_mmsp_mod[act]:<15.1f} | {g_cnod[act]:<10.1f}%")
    print("-" * 78)

    print("\nСводные метрики погрешностей:")
    print(f"• Алгоритм ЦНОД:      Дифф. ош. = {diff_cnod:.1f}%,  Интегр. ош. = {int_cnod:.1f}%,  Средняя добротность = {sum(g_cnod.values())/4:.1f}%")
    print(f"• ММСП (базовый):    Дифф. ош. = {diff_mmsp_c:.1f}%,  Интегр. ош. = {int_mmsp_c:.1f}%,  Средняя добротность = {sum(g_mmsp_c.values())/4:.1f}%")
    print(f"• ММСП (модифиц.):   Дифф. ош. = {diff_mmsp_m:.1f}%,  Интегр. ош. = {int_mmsp_m:.1f}%,  Средняя добротность = {sum(g_mmsp_m.values())/4:.1f}%")


if __name__ == "__main__":
    main()