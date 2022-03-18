def hello(name):
    return f"Hello {name}"

def dodaj() -> float:
    print('Podaj pierwszą liczbę:')
    a = input
    print('Podaj drugą liczbę: ')
    b = input
    return a + b


print(hello("Oskar"))