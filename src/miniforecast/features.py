"""Enkel feature-kod för tidsserier."""

import numpy as np


def moving_average(values: list[float], window: int) -> list[float]:
    """Glidande medelvärde. Ger len(values) - window + 1 värden."""
    if window < 1 or window > len(values):
        raise ValueError("window måste vara mellan 1 och antalet värden")
    array = np.asarray(values, dtype=float)
    kernel = np.ones(window) / window
    return np.convolve(array, kernel, mode="valid").tolist()


def min_max_scale(values: list[float]) -> list[float]:
    """Skala värdena till intervallet 0 till 1."""
    low, high = min(values), max(values)
    if low == high:
        raise ValueError("alla värden är lika, kan inte skala")
    return [(value - low) / (high - low) for value in values]
