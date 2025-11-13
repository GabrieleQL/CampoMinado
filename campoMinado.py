import random
import time
import os

PositionBombAndClean = "💣💣💣💣💣💣💣💣💣💣⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜"
band = "🚩"
emojiVencer = "😎"
emojiJogando = "🙂"
emojiPerder = "😞"

bandeira = 10

figuras = list(PositionBombAndClean)

print("."*40)
print("💣 Jogo do Campo Minado 💣")
print("."*40)

nomeJogador = input("Informe o seu nome: ")


jogo = []
escolhas = []

def preencheMatriz():
    for i in range(9):
        jogo.append([])
        escolhas.append([])
        for _ in range(9):
            num = random.randint(0, len(figuras)-1)
            jogo[i].append(figuras[num])
            escolhas[i].append("🟦")
            figuras.pop(num)

def mostraTabuleiro():
    os.system("cls")
    print(f"               🚩 {bandeira}           ")
    print("   1   2   3   4   5   6   7   8   9")
    for i in range(9):
        print(f"{i+1}",end="")
        for j in range(9):
            print(f" {escolhas[i][j]} ",end="")
        print("\n")

def mostraGabarito():
    os.system("cls")
    print("   1   2   3   4   5   6   7   8   9")
    for i in range(9):
        print(f"{i+1}",end="")
        for j in range(9):
            print(f" {jogo[i][j]} ",end="")
        print("\n")

###################################
#        Chamando as defs         #
##################################

preencheMatriz()
mostraTabuleiro()

tempoInicial = time.time()

def fazEscolhas(num):
    while True:
        mostraTabuleiro()
        posicao = input(f"{num}ª Coordenada (2 números: linha e coluna): ")
        if len(posicao) != 2:
            print("Informe uma dezena, por exemplo, 12, 24, 31, ...")
            time.sleep(2)
            continue
        x = int(posicao[0])-1
        y = int(posicao[1])-1

        try:
            if escolhas[x][y] == "🟦":
                escolhas[x][y] = jogo[x][y]
                break
            else:
                print("Coordenada já escolhida... escolha outra")
                time.sleep(2)
        except IndexError:
            print("Coordenada Inválida... repita")
            time.sleep(2)
    return x, y

def verificaTabuleiro():
    faltam = 0
    for i in range(9):
        for j in range(9):
            if escolhas[i][j] == "🟦":
                faltam += 1
    return faltam

while True:
    x, y = fazEscolhas(1)
    mostraTabuleiro

    #💣
    if escolhas[x][y] == "⬜":
        print("OK")
        contador = verificaTabuleiro()
        if contador == 0:
            print("VENCEU \O/")
            break
        else:
            print(f"Faltam {contador} posições para marcar")
            time.sleep(0.5)
    else:
        mostraGabarito()
        print("💣 BOOMMMMM ")
        break

tempoFinal = time.time()
duracaoJogo = tempoFinal - tempoInicial

print()
print("*"*40)
print(f"Jogador: {nomeJogador}")
print(f"Duração do Jogo: {int(duracaoJogo)} segundos")
print("*"*40)