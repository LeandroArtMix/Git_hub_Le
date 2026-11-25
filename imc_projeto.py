import os
os.system("cls")

peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

if altura <= 0:
    print("Altura invalida.")
else:
    imc = peso / (altura ** 2)
    print(f"Seu IMC e: {imc:.2f}")

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidade")