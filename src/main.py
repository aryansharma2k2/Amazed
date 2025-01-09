from window import Window
from point import Point
from line import Line
from cell import Cell

def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.draw(125, 125, 200, 200)

    c3 = Cell(win)
    c3.has_bottom_wall = False
    c3.draw(225, 225, 250, 250)

    c4 = Cell(win)
    c4.has_top_wall = False
    c4.draw(300, 300, 500, 500)
    
    c1.draw_move(c2)

    win.wait_for_close()
    
    
main()