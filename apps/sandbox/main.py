import sys
from nxcli import parse_args

desc = {
    "foo": str
}


def main():
    args = parse_args(sys.argv, desc)
    print(args.inputs)
    print(args.foo)
    print(args.valid())


if __name__ == "__main__":
    main()
