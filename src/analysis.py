import numpy as np

TAU = 2*np.pi

def get_data(n: int = 100) -> tuple[np.ndarray, np.ndarray]:
    x = np.linspace(0, 10, n)
    y = np.sin(TAU*x)
    return x, y