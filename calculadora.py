

import math


while True:

    operacao= input(print("Selecione a operação: \n1. Somar \n2. Subtrair \n3. Multiplicar \n4. Dividir \n5. Exponenciação \n6. Raiz Quadrada \n7. Logaritmo"))

    if operacao==("6"):
        numero1=float(input ("escolha o numero:"))

    elif operacao != ("6"):
        numero1=float(input ("escolha o numero: "))
        numero2=float(input ("escolha outro numero: "))
    
    
    if operacao == "1":
        resultado =numero1 +numero2
        print(resultado)
    elif operacao =="2":
        resultado = numero1 - numero2
        print(resultado)
    elif operacao == "3":
        resultado= numero1 * numero2
        print(resultado)
    elif operacao == "4":
        resultado = numero1 / numero2
        print(resultado)
    elif operacao =="5":
        resultado = numero1 ** numero2
        print(resultado)
    elif operacao == "6":
        resultado = numero1 ** 0,5
        print(f"A raiz quadrada de {numero1} é {resultado:.2f}")

    continuar = input("bora mais uma? '1' ou '2'")

    if continuar == ("1"):
        print('continuando')
    
    else:
        continuar==("2")
        print("encerrando")
        break







