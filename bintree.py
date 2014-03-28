"""
Recall that a linked list can be defined recursively as
either the empty list, or a pair of values where the first
value is the head of the list and the second value is
the tail of the list - this was an exercise you did a while
ago.

A binary tree can be defined recursively as well - a binary
tree is either an empty leaf node (represented by None), or a
3-tuple where the first element is the value, the second
element is another tree, and the third element is another tree.
The tree:

   a
  / \
  b  *
 / \
*   *
  
Can be represented as:

(a, (b, None, None), None)

With that in mind, write the following functions (and test them).
ASSUME ALL TREES ARE BINARY SEARCH TREES.

Using recursion will help greatly. An example:

def number_of_values(t):
    if not t: # If the tree is None, meaning it is a leaf
        return 0
    else:
        _, left, right = t
        return 1 + number_of_values(left) + number_of_values(right)
"""
#!/usr/bin/env python
import unittest

class CustomException(Exception):

    def __init__(self, value):

        self.parameter = value

    def __str__(self):

        return repr(self.parameter)

def raise_empty_tree_exception():

    raise CustomException("Empty tree detected!")

def get_values(t):
    if not t:
        return []
    x, left, right = t
    return [x] + get_values(left) + get_values(right)

def sum_tree(t):
    if not t:
        return 0
    x, left, right = t
    return x + sum_tree(left) + sum_tree(right)
    
def average_tree(t):
    return sum_tree(t) / number_of_values(t)

def min_element(t):
    try: 
        x, left, right = t
        if left == None: return x
        else: return min_element(left)
    except:
        raise_empty_tree_exception
        
    
def max_element(t):
    try: 
        x, left, right = t
        if right == None: return x
        else: return max_element(right)
    except:
        raise_empty_tree_exception
        
    
    
def insert(elem, t):
    if not t: return (elem, None, None)
    x, left, right = t
    if elem < x:
        return (x, insert(elem, left), right)
    else:
        return (x, left, insert(elem, right))

    
def contains(elem, t):
    if not t: return False
    x, left, right = t
    if elem == x: return True
    elif elem < x:
        return contains(elem, left)
    elif elem > x:
        return contains(elem, right)
    
    
def from_list(xs):
    u = tuple()
    for i in xs:
        u = insert(i, u)
    return u

class TestRun(unittest.TestCase):
    def setup(self):
        pass
    
    def test1(self):
        self.assertEqual(get_values( ( ( 3, (2, (1, None, None), None), (4, None, None) ) )), [3,2,1,4])
    
    def test2(self):
        self.assertEqual(sum_tree( ( ( 3, (2, (1, None, None), None), (4, None, None) ) )), 10)    

    def test3(self):
        self.assertEqual(min_element( ( ( 3, (2, (1, None, None), None), (4, None, None) ) )), 1)   

    def test4(self):
        self.assertEqual(max_element( ( ( 3, (2, (1, None, None), None), (4, None, None) ) )), 4)   

    def test5(self):
        self.assertEqual(insert(5, ( ( 3, (2, (1, None, None), None), (4, None, None) ) )), ( ( 3, (2, (1, None, None), None), (4, None, (5, None,None) ) )))   

    def test6(self):
        self.assertEqual(insert(5, ( ( 8, (7, (6, None, None), None), (9, None, None) ) )), ( ( 8, (7, (6, (5, None, None), None), None), (9, None, None) )))
    
    def test7(self):
        self.assertEqual(insert(5, tuple( )), (5, None, None))
        
    def test8(self):
        self.assertEqual(insert(4, (5, None, None)), (5, (4, None, None), None))
    
    def test9(self):
        self.assertEqual(insert(4, tuple()), (4, None, None))
    
    def test10(self):
        self.assertTrue(contains(4, ( ( 3, (2, (1, None, None), None), (4, None, None) ) ))) 
    
    def test11(self):
        self.assertFalse(contains(8, ( ( 3, (2, (1, None, None), None), (4, None, None) ) ))) 
    
    def test12(self):
        self.assertEqual(from_list([3,2,1,4]), ( (3, (2, (1, None, None), None), (4, None, None) )))
        
    def test13(self):
        self.assertRaises(CustomException, min_element( tuple()))

    def test14(self):
        self.assertRaises(CustomException, max_element( tuple()))  

    def teardown(self):
        pass

if __name__ == '__main__':
    unittest.main()