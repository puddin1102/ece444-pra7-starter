def add(a, b):
    return a + b


def record(value, history=None):
    if history is None:
        history = []
    history.append(value)
    return history


def is_zero(value):
    return value == 0


def broken_total():
    missing_total = 0
    return missing_total
