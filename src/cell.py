from line import Line
from point import Point

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        line1 = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self._win.draw_line(line1,"red")
        else:
            self._win.draw_line(line1,"white")
        line2 = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self._win.draw_line(line2,"red")
        else:
            self._win.draw_line(line2,"white")
        line3 = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self._win.draw_line(line3,"red")
        else:
            self._win.draw_line(line3,"white")
        line4 = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self._win.draw_line(line4,"red")
        else:
            self._win.draw_line(line4,"white")

    def draw_move(self, to_cell, undo=False):
        src_x = self._x1 + 0.5*(self._x2-self._x1)
        src_y = self._y1 + 0.5*(self._y2-self._y1)

        des_x = to_cell._x1 + 0.5*(to_cell._x2-to_cell._x1)
        des_y = to_cell._y1 + 0.5*(to_cell._y2-to_cell._y1)

        l = Line(Point(src_x,src_y), Point(des_x,des_y))
        color="red"
        if undo:
            color="gray"
        self._win.draw_line(l,color)

