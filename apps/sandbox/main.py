import nxmath


def main():
    values = [4, 8, 15, 16, 23, 42]
    print(nxmath.mean(values))
    print(nxmath.std_dev(values))
    print(nxmath.z_score(values, 30))


if __name__ == "__main__":
    main()
