from cell import Cell
import time
import random
class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1=x1
        self._y1=y1
        self._num_rows=num_rows
        self._num_cols=num_cols
        self._cell_size_x=cell_size_x
        self._cell_size_y=cell_size_y
        self._win=win
        if seed!=None:
            self._seed = random.seed(seed)
        
        self._cells=[]
        self._create_cells()

    
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
        self._break_entrance_and_exit()
        self.break_walls_r(0,0)
        self._reset_cells_visited()
    
    def _draw_cell(self,i,j):
        if self._win is None:
            return
        x1,y1 = self._x1+(i*self._cell_size_x), self._y1+(j*self._cell_size_y)
        x2,y2 = x1 + self._cell_size_x, y1 + self._cell_size_y
    
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()
        

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)


        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)
    
    def break_walls_r(self,i,j):
        self._cells[i][j]._visited = True
        while True: 
            ls=[]
            if self.check(i,j+1) and not self._cells[i][j+1]._visited:
                ls.append((i,j+1))
            if self.check(i+1,j) and not self._cells[i+1][j]._visited:
                ls.append((i+1,j))
            if self.check(i,j-1) and not self._cells[i][j-1]._visited:
                ls.append((i,j-1))
            if self.check(i-1,j) and not self._cells[i-1][j]._visited:
                ls.append((i-1,j))
            if len(ls)==0:
                self._draw_cell(i,j)
                return
            direction = random.choice(ls)
            print(direction)
            if direction[0]>i:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._draw_cell(direction[0],direction[1])
            elif direction[0]<i:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._draw_cell(direction[0],direction[1])
            elif direction[1]>j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._draw_cell(direction[0],direction[1])
            else:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._draw_cell(direction[0],direction[1])
                
            self.break_walls_r(direction[0],direction[1])

    def check(self,i,j):
        if 0<=i<self._num_cols and 0<=j<self._num_rows:
            return True
        return False

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited=False

