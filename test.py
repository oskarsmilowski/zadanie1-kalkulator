def hello(name):
    return f"Hello {name}"


def main():
    print("Podaj swoje imię: ")
    imie = input()
    print(hello(imie))
    print("Wybierz co chcesz zrobić?\n 1 - Dodaj dwie liczby \n 2 - Odejmij dwie liczby \n 9 - Zakończ")
    wybor = int(input())
    if wybor == 1:
        dodaj()
    elif wybor == 2:
        odejmij()
    elif wybor == 9:
        return
    else:
        print("Nieprawidłowy wybór")
        return


if __name__ == '__main__':
    main()