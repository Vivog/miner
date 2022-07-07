import random
class Cell:
    def __init__(self, around_mines, mine: bool):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


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
        # print(mines_pos)
        pole = []
        for i in self.var:
            if pos in mines_pos:
                pole.append(Cell(0, True))
            else:
                pole.append(Cell(0, False))
            pos += 1
        return pole

    def s_pole(self):
        pole = self.around_mines()
        while len(pole):
            self.pole.append(list(pole[:self.N]))
            del pole[:self.N]
        return self.pole


    def init(self):
        self.pole = self.s_pole()
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                if self.pole[i][j].mine == True:
                    if i == 0:
                        if j == 0:
                            self.pole[i][j + 1].around_mines += 1
                            self.pole[i + 1][j].around_mines += 1
                            self.pole[i + 1][j + 1].around_mines += 1
                        if j == len(self.pole[i]) - 1:
                            self.pole[i][j - 1].around_mines += 1
                            self.pole[i + 1][j].around_mines += 1
                            self.pole[i + 1][j - 1].around_mines += 1
                        if (len(self.pole[i]) - 1) > j > 0:
                            self.pole[i][j + 1].around_mines += 1
                            self.pole[i][j - 1].around_mines += 1
                            self.pole[i + 1][j].around_mines += 1
                            self.pole[i + 1][j + 1].around_mines += 1
                            self.pole[i + 1][j - 1].around_mines += 1
                    if i == len(self.pole) - 1:
                        if j == 0:
                            self.pole[i][j + 1].around_mines += 1
                            self.pole[i - 1][j].around_mines += 1
                            self.pole[i - 1][j + 1].around_mines += 1
                        if j == len(self.pole[i]) - 1:
                            self.pole[i][j - 1].around_mines += 1
                            self.pole[i - 1][j].around_mines += 1
                            self.pole[i - 1][j - 1].around_mines += 1
                        if(len(self.pole[i]) - 1) > j > 0:
                            self.pole[i][j + 1].around_mines += 1
                            self.pole[i][j - 1].around_mines += 1
                            self.pole[i - 1][j].around_mines += 1
                            self.pole[i - 1][j + 1].around_mines += 1
                            self.pole[i - 1][j - 1].around_mines += 1
                    if (len(self.pole) - 1) > i > 0:
                        if j == 0:
                            self.pole[i][j + 1].around_mines += 1
                            self.pole[i - 1][j].around_mines += 1
                            self.pole[i - 1][j + 1].around_mines += 1
                            self.pole[i + 1][j].around_mines += 1
                            self.pole[i + 1][j + 1].around_mines += 1
                        if j == len(self.pole[i]) - 1:
                            self.pole[i][j - 1].around_mines += 1
                            self.pole[i - 1][j].around_mines += 1
                            self.pole[i - 1][j - 1].around_mines += 1
                            self.pole[i + 1][j].around_mines += 1
                            self.pole[i + 1][j - 1].around_mines += 1
                        if (len(self.pole[i]) - 1) > j > 0:
                            self.pole[i][j + 1].around_mines += 1
                            self.pole[i][j - 1].around_mines += 1
                            self.pole[i - 1][j].around_mines += 1
                            self.pole[i - 1][j + 1].around_mines += 1
                            self.pole[i - 1][j - 1].around_mines += 1
                            self.pole[i + 1][j].around_mines += 1
                            self.pole[i + 1][j + 1].around_mines += 1
                            self.pole[i + 1][j - 1].around_mines += 1

    def show(self):
        for i in self.pole:
            for j in i:
                if j.fl_open == False:
                    print('#', end=' ')
                else:
                    if j.mine == True:
                        print('*', end=' ')
                    else:
                        print(j.around_mines, end=' ')
            print()


pole_game = GamePole(10, 12)
pole_game.show()

