from typing import Optional

class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def divide(self, a: float, b: float) -> Optional[float]:
        if b == 0:
            return None
        return a / b
