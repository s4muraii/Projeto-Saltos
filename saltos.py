# EXECICIO 02: O software tem o objetivo de salvar os valores dos saltos, calcular a média finais, e caso seja necessário o arbitro pode realizar a alteração dos valores.

#MENU INICIAL

import os

m = "N"
paticipantes = {}
x = 0

#LÓGICA DO REGISTRO

def registro (s):
    os.system("cls")
    name = input("Digite o nome do participante: ")
    z = int(input("Digite quantos saltos o participante fez: "))
    val = []
    for num in range(z):
        num = float(input("Digite a distancia do salto: "))
        val.append(num)
        paticipantes[name] = val
        os.system("cls")

#LÓGICA DA ALTERAÇÂO

def alteracao (s):
    os.system("cls")
    name = input("Digite o nome do participante: ")
    if name in paticipantes:
        print(f"Digite qual dos valores da lista deseja alterar")
        p = int(input(""))
        paticipantes[name][p] = float(input("Digite o novo valor: "))
        os.system("cls")
    else:
        print("Participante não encontrado")
        os.system("pause")

        os.system("cls")

#LÓGICA DA LISTAGEM

def listar (s):
    os.system("cls")
    for name, saltos in paticipantes.items():
        soma_saltos = 0
        qtd_saltos = 0
        for salto in saltos:
            soma_saltos += salto
            qtd_saltos += 1
        media = soma_saltos / qtd_saltos
        print(f"{name}: {saltos}, Média: {media}")
    os.system("pause")

    os.system("cls")

while m != "S":
    print("Bem-Vindo ao Software de saltos!  \n 1- Registro \n 2- Alterar \n 3- Listar \n 4- Sair")
    s = int(input("Digite a opção do Menu Inicial: "))

#REGISTRO

    if s == 1:
        registro(s)
        x = 1

#ALTERAÇÂO
    if s == 2:
        alteracao (s)

#LISTAR OS PARTICIPANTES
    elif s == 3 and x == 0:
         print("Você ainda não cadastrou nenhum Competidor")
    elif s == 3 and x != 0:
        listar(s)

#sAIR
    elif s == 4:
        m = "S"
    else:

        os.system("cls")

        print("Esta opção não está na lista")
