# A category tree is a representation of a set of categories and their parent-child relationships. Each category has a unique name (no two categories have the same name). A category can have a parent category. Categories without a parent category are called root categories .
# To add  a  category to a category tree, the name and the parent of the category should be provided. When adding a root category, a None value should be provided as the parent. A call to get_children should return an array containing the direct children of the specified category in any order.
# KeyError should be thrown when adding a category that has already been added anywhere in the CategoryTree or if a parent is specified but does not exist.
# For example:

#  c = CategoryTree()
#     c.add_category('A', None)
#     c.add_category('B', 'A')
#     c.add_category('C', 'A')
#     print(str(c))
#     print(','.join(c.get_children('A') or []))

# Running this code should display 'B,C' or 'C,B'.

# Implement the add_category and get_children methods of the CategoryTree class.

def recursive_find_parent(root, parentValue):
  if root.value == parentValue:
    return root
  else:
    for child in root.children:
      if child.value == parentValue:
        return child
      else: 
        return recursive_find_parent(child, parentValue)
      
def recursive_print(root, str=''):
  if (root != None):
    str += root.value
    for child in root.children:
      str += recursive_print(child, '')
  return str


class Category:
  def __init__(self, value, parent = None):
    self.value = value
    self.children = []
    if parent != None:
      self.parent = recursive_find_parent(self, parent)
    else:
      self.parent = None

class CategoryTree:

    def __init__(self):
      self.root = None
      
    def __str__(self):
      return recursive_print(self.root, '')

    def add_category(self, category, parent):
      new_category = Category(category, parent)
      if self.root == None:
        self.root = new_category
      else:
        # find the parent category and append new category as child
        parent = recursive_find_parent(self.root, parent)
        parent.children.append(new_category)
    def get_children(self, parent):
      children = recursive_find_parent(self.root, parent).children
      str = []
      for child in children:
        str.append(child.value)
      return str

if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(str(c))
    print(','.join(c.get_children('A') or []))