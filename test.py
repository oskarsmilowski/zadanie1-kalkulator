def hello(name):
    return f"Hello {name}"

def dodaj() -> float:
    print('Podaj pierwszą liczbę:')
    a = input()
    print('Podaj drugą liczbę: ')
    b = input()
    return a + b

def odejmij() -> float:
    print('Podaj liczbę od której chcesz odjąć')
    a = input()
    print('Podaj liczbę odejmowaną')
    b = input()
    return float(a) - float(b)

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
        return
    else:
        print("Nieprawidłowy wybór")
        return


if __name__ == '__main__':
    main()




