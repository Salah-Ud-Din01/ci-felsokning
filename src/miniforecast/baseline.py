"""Baslinjemodell: förutsäger medelvärdet av historiken."""

import os


def predict_mean(history: list[float], horizon: int) -> list[float]:
    """Förutsäg medelvärdet av historiken för varje steg framåt."""
    if not history:
        raise ValueError("historiken är tom")
    mean = sum(history) / len(history)
    return [mean] * horizon
