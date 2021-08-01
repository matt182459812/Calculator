#funzione addizione
def add(x, y):
    return x + y

#funzione sottrazione
def subtract(x, y):
    return x - y

#funzione moltiplicazione
def multiply(x, y):
    return x * y

#funzione divisione
def divide(x, y):
    return x / y

print('█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ ▀█▀ █▀█ █▀█')
print('█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ ░█░ █▄█ █▀▄')
print('                                       ')
print('                                       ')
print('                                       ')
print('                                       ')
print('  █▄▄ █▄█   █▀█ █░░ █░█ ▀█▀ █▀█ █▄░█ ')
print('  █▄█ ░█░   █▀▀ █▄▄ █▄█ ░█░ █▄█ █░▀█ ')
print('                                       ')

print('Menu Operatori')
print('1 = Addizione')
print('2 = Sottrazione')
print('3 = Moltiplicazione')
print('4 = Divisione')

while True:
    #Input dell'utente
    operatore = input("Scegli operatore: ")

    #controlla se la scelta è una delle opzioni
    if operatore in('1', '2', '3', '4'):
        num1 = float(input('Inserisci il primo numero: '))
        num2 = float(input('Inserisci il secondo numero: '))

        if operatore == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            input("Premere un tasto per uscire...")
        elif operatore == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            input("Premere un tasto per uscire...")

        elif operatore == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            input("Premere un tasto per uscire...")

        elif operatore == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
            input("Premere un tasto per uscire...")
        break
    else:
        print("Input Invalido")
#per runnare aprire powershell e scrivere 'python calc.py'


