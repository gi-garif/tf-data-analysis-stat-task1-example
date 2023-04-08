import pandas as pd
import numpy as np
from numpy import random


chat_id = 33217853 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    # Ваш ответ
    n = len(x)
    t = 10
    error = np.random.rand(0,1,n)
    a = 2*(x+error)/t**2
    return np.mean(a)

