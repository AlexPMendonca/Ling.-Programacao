# 2) Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam 
# ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso
#os valores formem um triângulo, calcular e escrever a área deste triângulo. Se
#não formam triângulo escrever os valores lidos. (Se a &gt; b + c não formam
#triângulo algum, se a é o maior).

import math


a = int(input("Digite o valor de a (lado 1): "))
b = int(input("Digite o valor de b (lado 2): "))
c = int(input("Digite o valor de c (lado 3): "))

if a < b + c and b < a + c and c < a + b:
    # Calcula a área do triângulo
    s = (a + b + c) / 2  
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Os valores formam um triângulo e sua área é: {area:.2f}")
else:
    print(f"Os valores não formam um triângulo: {a}, {b}, {c}")
    #Alex Mmendonca 

