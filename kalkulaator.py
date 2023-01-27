
# See funktsioon liidab numbreid
def add(x, y):
    return x + y
# See funktsioon lahutab numbrid
def subtract(x, y):
    return x - y
# See funktsioon korrutab numbreid
def multiply(x, y):
    return x * y
# See funktsioon jagab numbreid
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Liitmine")
print("2.Lahutamine")
print("3.Korrutamine")
print("4.Jagamine")
print("5.Keskmise arvutamine")
while True:
    # Siin sa valid millist sa tahad arvutada
    choice = input("Kirjuta valik(1/2/3/4/5): ")

    # Vaatab kas valik on ühes neist numbrites
    if choice in ('1', '2', '3', '4','5'):
        try:
            num1 = float(input("Sisesta esimene number: "))
            num2 = float(input("Sisesta teine number: "))
        except ValueError:
            print("Vigane sisestus. Palun sisesta number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "+", num2, "=", [add(num1, num2)/2])
        # Vaatab kas kasutaja tahab teist kalkulaatorit
        # Lõppetab tsükli kui kasutaja kirjutab ei
        next_calculation = input("Kas teeme järgmise tehte? (jah/ei): ")
        if next_calculation == "ei":
            break
    else:
        print("Vigane sisestus")
