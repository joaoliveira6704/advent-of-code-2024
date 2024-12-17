import os
# Constantes do jogo
linhas = 6
colunas = 7
# Listas 
listaLinhas = []
listaColunas = []


# Funções de inicialização do tabuleiro
def criarTabuleiro():
    """Cria um tabuleiro vazio com 6 linhas e 7 colunas."""
    for i in range(linhas):
        listaLinhas.append([])
        for j in range(colunas):
            listaColunas.append([])
        return listaColunas
    return listaLinhas
    

def imprimirTabuleiro(tabuleiro):
    """ Imprimir o tabuleiro """
    os.system('cls')  # Limpa a tela para atualizar o tabuleiro
    for i in range(colunas):
        print(('| ' + 'X ' + '| O ')*7)
        print('-' * 15*3)  # Linha inferior
    for i in range(colunas):
        print(str(i + 1) + " ", end="") # Print dos numeros respetivos a cada coluna


def obter_jogada(jogador):
    """ Pede uma coluna e verifica se é valida """
    while True:
        try:
            coluna = int(input(f"{jogador}, escolha uma coluna (1-7): ")) - 1
            if 0 <= coluna < colunas:
                return coluna
            else:
                print("Coluna Invalida, tente novamente.")
        except ValueError:
            print("Insira um número válido.")


# Obtem os nomes de cada jogador e atribui um simbolo
jogador1 = input("Nome do Jogador 1: ")
jogador2 = input("Nome do Jogador 2: ")
simbolo1 = 'X'
simbolo2 = 'O'

tabuleiro = criarTabuleiro()
imprimirTabuleiro(tabuleiro)
    
jogadorAtual = jogador1
simboloAtual = simbolo1