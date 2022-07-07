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
        self.var = range(0, self.N * self.N)
        self.init()

    def mines_pos(self):
        mines_pos = []
        while len(mines_pos) < self.M:
            mine = random.choice(self.var)
            if mine not in mines_pos:
                mines_pos.append(mine)
            else:
                continue
        return mines_pos

    def around_mines(self):
        pos = 0
        mines_pos = self.mines_pos()
        print(mines_pos)
        pole = []
        for i in self.var:
            if pos in mines_pos:
                pole.append(Cell(0, True))
            else:
                pole.append(Cell(0, False))
            pos += 1
        return pole



    def init(self):
        pole = self.around_mines()
        while len(pole):
            self.pole.append(list(pole[:self.N]))
            del pole[:self.N]
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                if self.pole[i][j].mine == True:
                    try:
                        self.pole[i][j - 1].around_mines += 1
                    except:
                        continue
                    try:
                        self.pole[i][j + 1].around_mines += 1
                    except:
                        continue
                    try:
                        self.pole[i-1][j - 1].around_mines += 1
                    except:
                        continue
                    try:
                        self.pole[i-1][j + 1].around_mines += 1
                    except:
                        continue
                    try:
                        self.pole[i-1][j].around_mines += 1
                    except:
                        continue
                    try:
                        self.pole[i+1][j - 1].around_mines += 1
                    except:
                        continue
                    try:
                        self.pole[i+1][j + 1].around_mines += 1
                    except:
                        continue
                    try:
                        self.pole[i+1][j].around_mines += 1
                    except:
                        continue

    def show(self):
        for i in self.pole:
            for j in i:
                if j.mine == True:
                    print('m', end=' ')
                else:
                    print(j.around_mines, end=' ')
            print()


pole_game = GamePole(10, 12)
pole_game.show()

