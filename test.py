def hello(name):
    return f"Hello {name}"


def main():
    print("Podaj swoje imię: ")
    imie = input()
    print(hello(imie))


if __name__ == '__main__':
    main()