import pandas as pd
import numpy as np

from scipy.stats import uniform


chat_id = 1171143592 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    a = 0.035
    return a + (x.max() - a)/(1 - uniform.ppf(alpha / 2)), \
           a + (x.max() - a)/(1 - uniform.ppf(1 - alpha / 2))
