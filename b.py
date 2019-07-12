from c import add
from testpack.d import sub


def main():
    x = 2
    y = 3
    z = add(x, y)
    print(z)
    z = sub(x, y)
    print(z)


if __name__ == '__main__':
    main()
