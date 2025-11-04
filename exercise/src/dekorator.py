from functools import wraps
import time
from typing import Set

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        total_time = time.perf_counter() - t0
        print("total_time:", total_time)
        return result
    return wrapper


def required_column(requireds: Set[str]):
    """Veri satırlarında belirtilen kolonların olup olmadığını kontrol eder."""
    def deco(func):
        @wraps(func)
        def wrapper(rows, *args, **kwargs):
            if not rows:
                raise ValueError("Boş veri seti")

            if not isinstance(rows[0], dict):
                raise TypeError("Beklenen veri tipi 'dict', ancak farklı bir tip alındı.")

            keys = set(rows[0].keys())
            missing = requireds - keys
            if missing:
                raise ValueError(f"Eksik kolon(lar): {', '.join(missing)}")

            return func(rows, *args, **kwargs)
        return wrapper
    return deco
