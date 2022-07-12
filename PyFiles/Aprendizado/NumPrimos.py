"""Faça um programa que leia um número e diga se ele é ou nao um numero primo
"""
while True:
    n = int(input("Digite um numero para ver se ele é primo: "))

    ti = 0
    for i in range(1, n + 1):
        if n % i == 0:
            print("\033[32m{}\033[m".format(i), end=" -> ")
            ti += 1
        else:
            print("\033[31m{}\033[m".format(i), end=" -> ")
    print("ACABOU!")

    if ti == 2:
        print("Esse número É PRIMO.")
    else:
        print("Esse número NÃO É PRIMO.")

    res = input("Quer Continuar?")
    if res in "Nn":
        break
