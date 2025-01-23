from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        #for debugging
        if seed is not None:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._solve_r(0, 0)
        


    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate(0.00)

    def _animate(self, x):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(x)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            #go left
            if i > 0 and self._cells[i - 1][j].visited == False:
                to_visit.append((i - 1, j))
            #go right
            if i < self._num_cols - 1 and self._cells[i+1][j].visited == False:
                to_visit.append((i + 1, j))
            #go down
            if j < self._num_rows - 1 and self._cells[i][j + 1].visited == False:
                to_visit.append((i, j + 1))
            #go up
            if j > 0 and self._cells[i][j - 1].visited == False:
                to_visit.append((i, j - 1))
            
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            
            dir_index = random.randrange(len(to_visit))
            new_idx = to_visit[dir_index]

            if new_idx[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            if new_idx[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False

            if new_idx[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
                
            if new_idx[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            

            self._break_walls_r(new_idx[0], new_idx[1])


    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False


    def solve(self):
        return self._solve_r(0, 0)
    
    
    def _solve_r(self, i, j):
        self._animate(0.05)

        self._cells[i][j].visited = True

        end_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        current_cell = self._cells[i][j]

        if current_cell == end_cell:
            return True
        
        #if theres a cell, no wall and not visited. draw a move
        #go right
        if (
            i < self._num_cols - 1
            and self._cells[i][j].has_right_wall == False
            and self._cells[i + 1][j].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i + 1, j) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        
        #go left
        if (
            i > 0
            and self._cells[i][j].has_left_wall == False
            and self._cells[i-1][j].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i - 1, j) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

        #go up
        if (
            j > 0
            and self._cells[i][j].has_top_wall == False
            and self._cells[i][j - 1].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j - 1) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)
        #go down
        if (
            j < self._num_rows - 1
            and self._cells[i][j].has_bottom_wall == False
            and self._cells[i][j + 1].visited == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j + 1) == True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)


        return False

        #if can't go anywhere return False


        
        







