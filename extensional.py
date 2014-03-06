#!/usr/bin/env python
import unittest

def empty_set():  return (lambda x: False)

def singleton(x):   return (lambda y: y == x)

def range_set(a, b):   return (lambda x: x > a and x < b)

def add(s, x): return (lambda y: s(y) or y == x)

def union(s1, s2): return (lambda x: s1(x) or s2(x))

def intersection(s1, s2): return (lambda x: s1(x) and s2(x))

def add_many(s, xs):
    return (lambda y: (s(y) or y in xs))

def add_range(s, l, u):
    return (lambda y: (s(y) or (l < y and y < u)))

def remove_range(s, l, u):
    return (lambda y: s(y) and (y < l or y > u))

def complement(s):
    return (lambda y: not s(y))

class TestRun(unittest.TestCase):
    def setUp(self):
        self.a = empty_set()
        self.b = singleton(3)
        self.c = range_set(2, 6)
        self.d = range_set(4, 10)
         
    def test_add_many(self):
        s = add_many(self.c, [6, 7, 8, 9])
        self.assertEqual(s(3), True)
        self.assertEqual(s(8), True)
        self.assertEqual(s(10), False)
        self.assertEqual(s(2), False)
    
    def test_add_range(self):
        s = add_range(self.c, 6, 9)
        self.assertEqual(s(3), True)
        self.assertEqual(s(8), True)
        self.assertEqual(s(10), False)
        self.assertEqual(s(2), False)        

    def test_remove_range(self):
        s = remove_range(self.d, 7, 9)
        self.assertEqual(s(5), True)
        self.assertEqual(s(8), False)
        self.assertEqual(s(6), True)
        self.assertEqual(s(10), False)
        
    def test_complement(self):
        s = complement(self.c)
        self.assertEqual(s(3), False)
        self.assertEqual(s(8), True)
        self.assertEqual(s(6), True)
        self.assertEqual(s(10), True) 

    def teardown(self):
        pass
 
if __name__ == '__main__':
    unittest.main()
