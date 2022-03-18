def hello(name):
    return f"Hello {name}"


def main():
    print("Podaj swoje imię: ")
    imie = input()
    print(hello(imie))
    print("Wybierz co chcesz zrobić?\n 1 - Dodaj dwie liczby \n 2 - Odejmij dwie liczby \n 9 - Zakończ")
    wybor = input()
    print(f"Twój wybór: {wybor}")


if __name__ == '__main__':
    main()