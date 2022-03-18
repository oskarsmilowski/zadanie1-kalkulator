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

print(hello("Oskar"))