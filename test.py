import random
class Cell:
    def __init__(self, around_mines, mine: bool):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = []
        self.init()
        self.var = range(0, self.N * self.N)

    def mines_pos(self):
        mines_pos = []
        while len(mines_pos) < self.M:
            mine = random.choice(self.var)
            if mine not in mines_pos:
                mines_pos.append(mine)
            else:
                continue
        print(mines_pos)
        return mines_pos

    def around_mines(self):
        pos = 0
        mines_pos = self.mines_pos()
        pole = []
        for i in self.var:
            if pos in mines_pos:
                pole.append(Cell(0, True))
            else:
                pole.append(Cell(0, False))


    def init(self):
        pos = 0
        mines_pos = self.mines_pos()
        for cell in range(0, self.N):
            self.pole.append([])
            for elem in range(0, self.N):
                if len(self.pole[cell]) < self.N:
                    if pos in mines_pos:
                        self.pole[cell].append(Cell(0, True))
                    else:
                        self.pole[cell].append(Cell(0, False))
                    pos += 1
        print(self.pole)




    def show(self):
        for i in self.pole:
            for j in i:
                if j.mine == True:
                    print('m', end=' ')
                else:
                    print('0', end=' ')
            print()


pole_game = GamePole(10, 12)
pole_game.show()

