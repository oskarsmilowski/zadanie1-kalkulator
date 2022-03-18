def hello(name):
    return f"Cześć {name}"


def main():
    print("Podaj swoje imię: ")
    imie = input()
    print(hello(imie))
    print("Wybierz co chcesz zrobić?\n 1 - Dodaj dwie liczby \n 2 - Odejmij dwie liczby \n 9 - Zakończ")
    wybor = int(input())
    if wybor == 1:
        wynik = dodaj()
        print(f"Wynik to: {wynik}")
    elif wybor == 2:
        wynik = odejmij()
        print(f"Wynik to: {wynik}")
    elif wybor == 9:
        return 0
    else:
        print("Nieprawidłowy wybór")
        return 1


if __name__ == '__main__':
    main()