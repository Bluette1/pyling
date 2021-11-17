import unittest
from src import category_tree as category_tree

class MyTestCase(unittest.TestCase):
    def test_category_tree(self):
        c = category_tree.CategoryTree()
        c.add_category('A', None)
        c.add_category('B', 'A')
        c.add_category('C', 'A')
        self.assertEqual(str(c), 'ABC', 'str(c)' )
        
    def test_category_tree_children(self):
        c = category_tree.CategoryTree()
        c.add_category('A', None)
        c.add_category('B', 'A')
        c.add_category('C', 'A')
        self.assertEqual(','.join(c.get_children('A') or []), 'B,C', '\',\'.join(c.get_children(%s) or [])' %('A'))
  
if __name__ == '__main__':
    unittest.main()
