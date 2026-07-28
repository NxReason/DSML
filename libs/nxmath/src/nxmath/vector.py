class Vector:
    def __init__(self, elements):
        self.elements = elements

    def __repr__(self):
        str_values = ', '.join([str(e) for e in self.elements])
        return f'Vector([{str_values}])'


def add(v1: Vector, v2: Vector) -> Vector:
    return Vector([x + y for (x, y) in zip(v1.elements, v2.elements)])


def sub(v1: Vector, v2: Vector) -> Vector:
    return add(v1, scalar_mult(v2, -1))


def scalar_mult(v: Vector, c: float) -> Vector:
    return Vector([x * c for x in v.elements])
