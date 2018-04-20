import numpy as np
def identity(n):
    return [ [0] * i + [1] + [0] * (n - i - 1) for i in range(n)]
