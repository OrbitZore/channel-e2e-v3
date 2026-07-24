"""Calculator module."""

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f"arguments must be int, got {type(a).__name__} and {type(b).__name__}")
    return a * b
