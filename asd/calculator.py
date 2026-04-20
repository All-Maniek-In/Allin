def add(x, y):
    """Dodawanie"""
    return x + y

def subtract(x, y):
    """Odejmowanie"""
    return x - y

def multiply(x, y):
    """Mnożenie"""
    return x * y

def divide(x, y):
    """Dzielenie"""
    if y == 0:
        return "Błąd: nie można dzielić przez zero!"
    return x / y

def main():
    print("--- Prosty Kalkulator ---")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    choice = input("Twój wybór (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Podaj pierwszą liczbę: "))
            num2 = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("To nie jest prawidłowa liczba!")
            return

        if choice == '1':
            print(f"Wynik: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Wynik: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Wynik: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Wynik: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Nieprawidłowy wybór")

if __name__ == "__main__":
    main()
