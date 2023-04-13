import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 973327975 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # Рассчитываем выборочное среднее для каждой выборки
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Рассчитываем выборочные стандартные отклонения для каждой выборки
    x_std = np.std(x, ddof=1)
    y_std = np.std(y, ddof=1)

    # Рассчитываем статистику критерия
    n = len(x)
    m = len(y)
    s_p = np.sqrt(((n - 1) * x_std ** 2 + (m - 1) * y_std ** 2) / (n + m - 2))
    t = (x_mean - y_mean) / (s_p * np.sqrt(1 / n + 1 / m))

    # Рассчитываем критическое значение
    alpha = 0.07
    df = n + m - 2
    t_crit = abs(np.round(s_p.t.ppf(alpha / 2, df), 2))

    # Сравниваем статистику критерия с критическим значением
    return abs(t) > t_crit
