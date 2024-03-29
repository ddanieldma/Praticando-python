"""
Comentários são feitos assim
Arquivozinhos de cria pra anotar varias coisas uteis de python p usar

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Fazendo imports de diferentes pastas
tem duas formas de fazê-lo

alterando o module interno sys, onde alteramos o sys.path, que, equivalentemente ao path do windows
é onde o programa olha para procurar por coisas importantes como os modules
"""
import sys
#como o sys.path é uma lista, podemos simplesmente adicionar o caminho do novo módulo
# sys.path.append('c:/Users/B51995/Desktop/Praticando-python/packageListas')
# sys.path.append('c:/Users/B51995/Desktop/Praticando-python/package')
# import funcoes as func

"""
agora, chamamos os módulos como se nada tivesse acontecido


É possível também, pelo terminal, mudar a variável de ambiente PYTHONPATH, mas eu preferi usar só
a forma que pode ser feita dentro do código

Mesmo que de um warning, isso ocorre porque o pre-analisador não entende que os modulos podem estar em outra pasta, mas por enquanto eu acho que nao tem problema
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

#Import para manipulação dos arquivos do sistema
import os
"""
modulos e packages --> modulos são o arquivo py, enquanto o package tem o arquivo __init__

imports de todos os modulos/arquivos com todo o código ja escrito para organizar
cada módulo faz uma coisa diferente e tem uma função que roda todo o código
"""


#Começando bem:
# func.saudacao()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Usamos a palavra-chave pass para permitir que um bloco de código com algo 
que ainda vai ser feito execute, mesmo sem fazer nada, sem gerar um erro, como de identação, por exemplo
"""
n = 11

if n > 10:
    pass

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#brincando com modules
#listar os bgl dentro de um modulo
# funcoes = dir (func)

#listar as variaveis modulos e os caralha4
print(dir())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Usando outras bases decimais
print(0b1101011)  # printa 107 em binário

print(0xFB + 0b10)  # soma hexadecimal com binpario = printa 253

print(0o15)  # printa 13 em octal

"""
binário: 0b ou 0B
octal: 0o ou 00
hexadecimal: 0x ou 0X
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Daqui p frente código dos outros módulos

#usando range
range = list(range(5, 30, 2))
print(range)

alunos = ["a", "b", "c", "d", "e", "Beatriz", "Itamar"]

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# procurando por um elemento dentro de uma lista
# procura por Beatriz
if "Beatriz" in alunos:
    print("achei!")
else:
    print("não :(")

# procura pela lista ["Beatriz", "Itamar"]
if ["Beatriz", "Itamar"] in alunos:
    print("achei!")
else:
    print("não :(")

# procura por beatriz e itamar na lista
if "Beatriz" in alunos and "Itamar" in alunos:
    print("achei!")
else:
    print("não :(")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
numero = 10
lista_teste = []
lista_teste.append(0 for i in range(numero))
print(lista_teste)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def fibonacci(n):

   temp1, temp2 = 0, 1

   total = 0

   while total < n:

       yield temp1

       temp3 = temp1 + temp2

       temp1 = temp2

       temp2 = temp3

       total += 1

fib_object = fibonacci(20)