import random
import os

class TicTacToe:
    def __init__(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.done = ""

    def print_board(self): #tabuleiro
        print(" ")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " + self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " + self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " + self.board[2][2])
       

    def reset(self): #resetar tabuleiro
        self.reset()

    def check_win_or_draw(self): #checkar quem ganhou
        dict_win = {}
        for i in ['X', '0']:
            #horizontais
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]
            # verticais
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]
            #verticais
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[1][1] == self.board[0][2] == i) or dict_win[i]

            if dict_win['X']:
                self.done = 'x'
                print('X Venceu')
                return
            elif dict_win['0']:
                self.done = '0'
                print('0 Venceu')
                return
            #empate
            c = 0
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] != ' ':
                        c += 1
                        break
            if c == 0:
                self.done = 'd'
                print('empate')
                return
    
    def get_player_move(self):
        invalid_move=True
        while invalid_move:
            try:
                print('Digite a linha do seu próximo lance')
                x = int(input())

                print('Digite a linha do seu próximo lance')
                y = int(input())

                if x > 2 or x < 0 or y > 0 or y < 0:
                    print('Coordenadas inválidas')
                if self.board[x][y] == ' ':
                    print('Posição já preenchida')
                    continue
            except Exception as e:
                print(e)
                continue
            invalid_move = False
        self.board[x][y] = 'X'

    def make_move(self):
        list_moves = []

        for i in range(3):
            for j in range(3):
                if self.board[i][i] == ' ':
                    list_move.append((i,j))
            if len(list_moves) > 0:
                x, y = random.choice(list_moves)
                self.board[x][y] = '0'
TicTacToe = TicTacToe()
TicTacToe.print_board()
next = 0

while next == 0:
    os.system('clear')
    TicTacToe.print_board()
    while TicTacToe.done == '':
        TicTacToe.get_player_move()
        TicTacToe.make_move()
        os.system('clear')
        TicTacToe.print_board()
        TicTacToe.check_win_or_draw()

    print('Digite 1 para sair do jogo ou qualquer tecla para continuar')

    next = int(input())
    if next == 1:
        break
    else:
        TicTacToe.reset()
        next = 0
  