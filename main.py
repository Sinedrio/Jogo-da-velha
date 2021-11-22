import os
#criar jogador
def criaJogador():
    nome = input('Digite o nome do novo jogador: ')

#verifica se um arquivo ja existe
    if os.path.isfile('{}.txt' .format(nome)):
        print('Jogador já registrado!\n')
    else:
        print('Registrando o jogador {}\n' .format(nome))
    f = open("{}.txt" .format(nome) , "w")
    f.write("0\n")      # sao as pontuação/vitórias
    f.write("0\n")      #aqui as derrotas
    f.close()




#ler historico do jogo
def lerHistorico():
    nome = input("Digite o nome do jogador: ")
    if os.path.isfile("{}.txt".format(nome)):
        f = open("{}.txt".format(nome), "r")
        print("Esta é a pontuação de {}: ".format(nome))
        historico = f.readlines()
        vitorias = int(historico[0])
        derrotas = int(historico[1])
        print("Vitórias: {}\n Derrotas: {}".format(vitorias, derrotas))
    else:
        print("Jogador {} não existe".format(nome))
#exlui jogador
def excluirJogador():
    nome = input ("Digite o nome do jogador a ser excluído: ")
#Verifica se o jogador excluído existe
    if os.path.isfile("{}.txt" .format(nome)):
        print ("Excluindo o jogador {} \n" .format(nome))
        os.remove("{}.txt" .format(nome))
    else:
        print ("Jogador {} não existe!\n" .format(nome))

#verificar se tem jogador para começar o jogo
def GO():
  primeiro=input("Digite o nome do primeiro jogador: ")
  if os.path.isfile("{}.txt".format(primeiro)):
    print("{} entrou no jogo!\n".format(primeiro))
  else:
    print("{} não registrado!\n".format(primeiro))
    return main()

  segundo=input("Digite o nome do segundo jogador: ")
  if os.path.isfile("{}.txt".format(segundo)):
    print("{} entrou no jogo!\n".format(segundo))
    pass
  else:
    print("{} não registrado!\n".format(segundo))
    return main()
#marcar pontos
def resultado():
 vencedor = input ('Se você quer registrar no seu histórico, por favor digite seu nome novamente: ')
 f = open('{}.txt'.format(vencedor), 'r')
 historico = f.readlines()
 f.close()
 vitorias = int(historico[0]) + 1
 derrotas = int(historico[1])
 f = open('{}.txt'.format(vencedor), 'w')
 f.write('{}\n{}'.format(vitorias, derrotas))
 f.close()
#perdedor
 perdedor = input ('Se você quer registrar no seu histórico, por favor digite seu nome novamente: ')
 f = open('{}.txt'.format(perdedor), 'r')
 historico = f.readlines()
 f.close()
 vitorias = int(historico[0])
 derrotas = int(historico[1]) + 1
 f = open('{}.txt'.format(perdedor), 'w')
 f.write('{}\n{}'.format(vitorias, derrotas))
 f.close()


#menu do jogo
def main():
    while True:
        print('-------MENU--------')
        print('1 - Criar novo usuário')
        print('2 - Exibir histórico do jogo')
        print('3 - Excluir jogador')
        print('4 - começar o jogo')
        break

    op= (input('Escolha uma das opções: '))
    if op == '1':
        criaJogador()
        return main()
    elif op == '2':
        lerHistorico()
        return main()
    elif op == '3':
        excluirJogador()
        return main()
    elif op== '4':
        GO()
    else:
        print('impossivel! escolha outra opção.')
        return main()

#execução do programa
main()

matriz = [
    [" "," "," "," "," "," "],
    [" "," "," "," "," "," "],
    [" "," "," "," "," "," "],
    [" "," "," "," "," "," "],
    [" "," "," "," "," "," "],
    [" "," "," "," "," "," "]
]

#Imprimindo o jogo para o usuário

def imprimirJogo():
    for i in range(0,26):
        tabuleiro = """
        Lin.
        0)  {}  | {} | {} | {} | {}
            ---+---+---+---+---
        1)  {}  | {} | {} | {} | {}
            ---+---+---+---+---
        2)  {}  | {} | {} | {} | {}
            ---+---+---+---+---
        3)  {}  | {} | {} | {} | {}
            ---+---+---+---+---
        4)  {}  | {} | {} | {} | {}
        
        Col.  0   1   2   3   4 
        """.format(matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], matriz[0][4],
        matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3], matriz[1][4],
        matriz[2][0], matriz[2][1], matriz[2][2], matriz[2][3], matriz[2][4],
        matriz[3][0], matriz[3][1], matriz[3][2], matriz[3][3], matriz[3][4],
        matriz[4][0], matriz[4][1], matriz[4][2], matriz[4][3], matriz[4][4])
        print(tabuleiro)
        #empate
        if i == 25:
            print('VELHA!!!!')
            return main()
        #ver quando é a vez de quem
        if i % 2 ==0:
            print('é a vez do primeiro jogador: ')
        else:
            print('é a vez do segundo jogador: ')

        linha = int(input('Digite o número da linha: '))
        coluna = int(input('Digite o número da coluna: '))

        #nao deixar colocar em lugar ocupado
        while matriz[linha][coluna] == 'X':
            print("Ops! Escolha outro lugar.")
            linha = int(input('Digite o número da linha: '))
            coluna = int(input('Digite o número da coluna: '))
        while matriz[linha][coluna] == 'O':
            print('Ops! Escolha outro lugar.')
            linha = int(input('Digite o número da linha: '))
            coluna = int(input('Digite o número da coluna: '))

        if i % 2 == 0:      #condicoes de vitoria player 1
            matriz[linha][coluna] = 'O'
            if matriz[0][0] == 'O' and matriz[0][1] == 'O' and matriz[0][2] == 'O' and matriz[0][3] == 'O':  # fim de uma possibilidade linha 0
               matriz[linha][coluna] = 'O'
               print('Primeiro jogador é o campeão!')
               resultado()
               return main()
            elif matriz[0][1] == 'O' and matriz[0][2] == 'O' and matriz[0][3] == 'O' and matriz[0][4] == 'O':  # fim de uma possibilidade linha 0
                 matriz[linha][coluna] = 'O'
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][0] == 'O' and matriz[1][1] == 'O' and matriz[1][2] == 'O' and matriz[1][3] == 'O':  # fim de uma possibilidade linha 1
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][1] == 'O' and matriz[1][2] == 'O' and matriz[1][3] == 'O' and matriz[1][4] == 'O':  # fim de uma possibilidade linha1
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[2][0] == 'O' and matriz[2][1] == 'O' and matriz[2][2] == 'O' and matriz[2][3] == 'O':  # fim de uma possibilidade linha2
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[2][1] == 'O' and matriz[2][2] == 'O' and matriz[2][3] == 'O' and matriz[2][4] == 'O':  # fim de uma possibilidade linha2
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[3][0] == 'O' and matriz[3][1] == 'O' and matriz[3][2] == 'O' and matriz[3][3] == 'O': # fim da linha 3
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é campeão!')
                 resultado()
                 return main()
            elif matriz[3][1] == 'O' and matriz[3][2] == 'O' and matriz[3][3] == 'O' and matriz[3][4] == 'O': # fim da linha 3
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é campeão!')
                 resultado()
                 return main()
            elif matriz[4][0] == 'O' and matriz[4][1] == 'O' and matriz[4][2] == 'O' and matriz[4][3] == 'O': # fim da linha 4
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é campeão!')
                 resultado()
                 return main()
            elif matriz[4][1] == 'O' and matriz[4][2] == 'O' and matriz[4][3] == 'O' and matriz[4][4] == 'O': # fim da linha 4
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é campeão!')
                 resultado()
                 return main()
            elif matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0] == 'O' and matriz[3][0] == 'O':  #coluna 0
                 matriz[linha][coluna] = 'O'
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][0] == 'O' and matriz[2][0] == 'O' and matriz[3][0] == 'O' and matriz[4][0] == 'O':  #coluna 0
                 matriz[linha][coluna] = 'O'
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][1] == 'O' and matriz[1][1] == 'O' and matriz[2][1] == 'O' and matriz[3][1] == 'O':  #coluna 1
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][1] == 'O' and matriz[2][1] == 'O' and matriz[3][1] == 'O' and matriz[4][1] == 'O':  #coluna 1
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][2] == 'O' and matriz[1][2] == 'O' and matriz[2][2] == 'O' and matriz[3][2] == 'O':  #coluna 2
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][2] == 'O' and matriz[2][2] == 'O' and matriz[3][2] == 'O' and matriz[4][2] == 'O':  #coluna 2
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][3] == 'O' and matriz[1][3] == 'O' and matriz[2][3] == 'O' and matriz[3][3] == 'O':  #coluna 3
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][3] == 'O' and matriz[2][3] == 'O' and matriz[3][3] == 'O' and matriz[4][3] == 'O':  #coluna 3
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][4] == 'O' and matriz[1][4] == 'O' and matriz[2][4] == 'O' and matriz[3][4] == 'O':  #coluna 4
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][4] == 'O' and matriz[2][4] == 'O' and matriz[3][4] == 'O' and matriz[4][4] == 'O':  #coluna 4
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == 'O' and matriz[3][3] == 'O':  #diagonal normal
                 matriz[linha][coluna] = 'O'
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][1] == 'O' and matriz[2][2] == 'O' and matriz[3][3] == 'O' and matriz[4][4] == 'O':  #diagonal normal
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][1] == 'O' and matriz[1][2] == 'O' and matriz[2][3] == 'O' and matriz[3][4] == 'O':  #diagonal normal
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][0] == 'O' and matriz[2][1] == 'O' and matriz[3][2] == 'O' and matriz[4][3] == 'O':  #diagonal normaal
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[4][0] == 'O' and matriz[3][1] == 'O' and matriz[2][2] == 'O' and matriz[1][3] == 'O':  #diagonal invertida
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[3][1] == 'O' and matriz[2][2] == 'O' and matriz[1][3] == 'O' and matriz[0][4] == 'O':  #diagonal invertida
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[3][0] == 'O' and matriz[2][1] == 'O' and matriz[1][2] == 'O' and matriz[0][3] == 'O':  #diagonal invertida
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[4][1] == 'O' and matriz[3][2] == 'O' and matriz[2][3] == 'O' and matriz[1][4] == 'O':  #diagonal invertida
                 matriz[linha][coluna] = 'O'
                 print(tabuleiro)
                 print('Primeiro jogador é o campeão!')
                 resultado()
                 return main()
            else:
                continue
        else: #condicoes de vitoria player 2
            matriz[linha][coluna]='X'
            if matriz[0][0] == 'X' and matriz[0][1] == 'X' and matriz[0][2] == 'X' and matriz[0][3] == 'X':  # fim de uma possibilidade linha 0
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][1] == 'X' and matriz[0][2] == 'X' and matriz[0][3] == 'X' and matriz[0][4] == 'X':  # fim de uma possibilidade linha 0
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][0] == 'X' and matriz[1][1] == 'X' and matriz[1][2] == 'X' and matriz[1][3] == 'X':  # fim de uma possibilidade linha 1
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][1] == 'X' and matriz[1][2] == 'X' and matriz[1][3] == 'X' and matriz[1][4] == 'X':  # fim de uma possibilidade linha1
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[2][0] == 'X' and matriz[2][1] == 'X' and matriz[2][2] == 'X' and matriz[2][3] == 'X':  # fim de uma possibilidade linha2
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[2][1] == 'X' and matriz[2][2] == 'X' and matriz[2][3] == 'X' and matriz[2][4] == 'X':  # fim de uma possibilidade linha2
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[3][0] == 'X' and matriz[3][1] == 'X' and matriz[3][2] == 'X' and matriz[3][3] == 'X': # fim da linha 3
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[3][1] == 'X' and matriz[3][2] == 'X' and matriz[3][3] == 'X' and matriz[3][4] == 'X': # fim da linha 3
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[4][0] == 'X' and matriz[4][1] == 'X' and matriz[4][2] == 'X' and matriz[4][3] == 'X': # fim da linha 4
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[4][1] == 'X' and matriz[4][2] == 'X' and matriz[4][3] == 'X' and matriz[4][4] == 'X': # fim da linha 4
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][0] == 'X' and matriz[1][0] == 'X' and matriz[2][0] == 'X' and matriz[3][0] == 'X':  #coluna 0
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][0] == 'X' and matriz[2][0] == 'X' and matriz[3][0] == 'X' and matriz[4][0] == 'X':  #coluna 0
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][1] == 'X' and matriz[1][1] == 'X' and matriz[2][1] == 'X' and matriz[3][1] == 'X':  #coluna 1
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][1] == 'X' and matriz[2][1] == 'X' and matriz[3][1] == 'X' and matriz[4][1] == 'X':  #coluna 1
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][2] == 'X' and matriz[1][2] == 'X' and matriz[2][2] == 'X' and matriz[3][2] == 'X':  #coluna 2
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][2] == 'X' and matriz[2][2] == 'X' and matriz[3][2] == 'X' and matriz[4][2] == 'X':  #coluna 2
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][3] == 'X' and matriz[1][3] == 'X' and matriz[2][3] == 'X' and matriz[3][3] == 'X':  #coluna 3
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][3] == 'X' and matriz[2][3] == 'X' and matriz[3][3] == 'X' and matriz[4][3] == 'X':  #coluna 3
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][4] == 'X' and matriz[1][4] == 'X' and matriz[2][4] == 'X' and matriz[3][4] == 'X':  #coluna 4
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][4] == 'X' and matriz[2][4] == 'X' and matriz[3][4] == 'X' and matriz[4][4] == 'X':  #coluna 4
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X' and matriz[3][3] == 'X':  #diagonal normal
                 matriz[linha][coluna] = 'X'
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][1] == 'X' and matriz[2][2] == 'X' and matriz[3][3] == 'X' and matriz[4][4] == 'X':  #diagonal normal
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[0][1] == 'X' and matriz[1][2] == 'X' and matriz[2][3] == 'X' and matriz[3][4] == 'X':  #diagonal normal
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[1][0] == 'X' and matriz[2][1] == 'X' and matriz[3][2] == 'X' and matriz[4][3] == 'X':  #diagonal normaal
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[4][0] == 'X' and matriz[3][1] == 'X' and matriz[2][2] == 'X' and matriz[1][3] == 'X':  #diagonal invertida
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[3][1] == 'X' and matriz[2][2] == 'X' and matriz[1][3] == 'X' and matriz[0][4] == 'X':  #diagonal invertida
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[3][0] == 'X' and matriz[2][1] == 'X' and matriz[1][2] == 'X' and matriz[0][3] == 'X':  #diagonal invertida
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            elif matriz[4][1] == 'X' and matriz[3][2] == 'X' and matriz[2][3] == 'X' and matriz[1][4] == 'X':  #diagonal invertida
                 matriz[linha][coluna] = 'X'
                 print(tabuleiro)
                 print('Segundo jogador é o campeão!')
                 resultado()
                 return main()
            else:
                continue

imprimirJogo()





