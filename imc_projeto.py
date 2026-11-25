import os
os.system("cls")

peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

imc = peso / (altura * altura)

print("Seu IMC é:", round(imc, 2))

if imc < 18.5:
    print("Classificacao: Abaixo do peso")
elif imc < 25:
    print("Classificacao: Peso normal")
elif imc < 30:
    print("Classificacao: Sobrepeso")
else:
    print("Classificacao: Obesidade")