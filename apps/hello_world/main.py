from nxmath import vector
from nxmath.vector import Vector
import plotter


def main():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    print(vector.sub(v1, v2))


if __name__ == "__main__":
    main()
