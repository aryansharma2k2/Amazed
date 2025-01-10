import unittest
from maze import Maze



class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_animate(self):
        num_cols = 15
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        self.assertEqual(
            m1._animate(),
            None,
        )

    def test_draw_cell(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        self.assertEqual(
            m1._draw_cell(0,0),
            None,
        )

if __name__=="__main__":
    unittest.main()