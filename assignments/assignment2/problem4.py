import random
from typing import List, Tuple, Optional

def train_test_split(seq: List, test_ratio: float, seed: Optional[int] = None) -> Tuple[list, list]:
   
    # Проверка на валидность test_ratio
    if not (0.0 <= test_ratio <= 1.0):
        raise ValueError("test_ratio должен быть между 0.0 и 1.0.")

    copied_seq = seq.copy()

    # Установка сида для воспроизводимости
    if seed is not None:
        random.seed(seed)
    
    # Перемешивание, если список не пуст
    if copied_seq:
        random.shuffle(copied_seq)
        
    cut_index = int(round(len(copied_seq) * (1.0 - test_ratio)))

    # Разделение
    train = copied_seq[:cut_index]
    test = copied_seq[cut_index:]
    
    return train, test
