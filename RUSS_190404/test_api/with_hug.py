import hug
import numpy as np

@hug.get(examples='samples=100')
@hug.local()
def mean(samples: hug.types.number = 10):
    data = np.random.randn(samples)
    return data.mean()

@hug.post()
@hug.local()
def sum(a: hug.types.number, b: hug.types.number):
    """Returns the result of adding number_1 to number_2"""
    return a + b

