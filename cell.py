from graphics import Line, Point, Window


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall == True:
            line = Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x1,y2))
            self._win.draw_line(line, "white")
        if self.has_right_wall == True:
            line = Line(Point(x2,y2), Point(x2,y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2,y2), Point(x2,y1))
            self._win.draw_line(line, "white")
        if self.has_top_wall == True:
            line = Line(Point(x1,y1), Point(x2,y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y1), Point(x2,y1))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall == True:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1,y2), Point(x2,y2))
            self._win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        #find centrum of self and make a point
        #find centrum of to_cell and make a point
        #make a line
        #draw the line
        half = abs(self._x2 - self._x1) // 2
        y_var = self._y1 + half
        x_var = self._x1 + half
        self_point = Point(x_var, y_var)

        half1 = abs(to_cell._x2 - to_cell._x1) // 2
        y_var2 = to_cell._y1 + half1
        x_var2 = to_cell._x1 + half1
        to_cell_point = Point(x_var2, y_var2)

        line = Line(self_point, to_cell_point)
        if undo:
            self._win.draw_line(line, "gray")
        else:
            self._win.draw_line(line, "red")



