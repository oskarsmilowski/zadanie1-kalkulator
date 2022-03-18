def hello(name):
    return f"Cześć {name}"

def dodaj() -> float:
    print('Podaj pierwszą liczbę:')
    a = float(input())
    print('Podaj drugą liczbę: ')
    b = float(input())
    return a+b

def odejmij() -> float:
    print('Podaj liczbę od której chcesz odjąć')
    a = float(input())
    print('Podaj liczbę odejmowaną')
    b = float(input())
    return a-b

def main():
    print("Podaj swoje imię: ")
    imie = input()
    print(hello(imie))
    print("Wybierz co chcesz zrobić?\n 1 - Dodaj dwie liczby\n 2 - Odejmij dwie liczby\n 9 - Zakończ")
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


