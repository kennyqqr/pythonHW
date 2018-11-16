import unittest
import pyClass

class TestInputType(unittest.TestCase):
    

    def test_py_x(self):
        py = pyClass.pyClass()
        py.setX(110)
        self.assertEqual(110, py.getX())
    
    def test_py_y(self):
        py = pyClass.pyClass()
        py.setY(35)
        self.assertNotEqual(110, py.getY())

    def test_global_var(self):
        py = pyClass.pyClass()
        self.assertEqual(py.getX()-py.getY(),-1)

if __name__ == '__main__':
    unittest.main()