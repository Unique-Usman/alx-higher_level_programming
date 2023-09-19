def add(x, y):
    """Add function"""
    return x + y

def sub(x, y):
    """Substract Function"""
    return x - y
def mul(x, y):
    """Multiply function"""
    return x * y
def div(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError("Can not divide by Zero")
    return x/y
