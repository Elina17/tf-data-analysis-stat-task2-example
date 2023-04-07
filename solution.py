import pandas as pd
import numpy as np

from scipy.stats import uniform
from scipy.stats import norm


chat_id = 1171143592 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    a = 0.035
    return 2*x.mean() - a - 2*np.sqrt(np.var(x)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x)), \
           2*x.mean() - a - 2*np.sqrt(np.var(x)) * norm.ppf(alpha / 2) / np.sqrt(len(x))
