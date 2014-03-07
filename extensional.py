#!/usr/bin/env python
import unittest
import math

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

def remove(s, x):
    return (lambda y: s(y) and (not y == x))

def remove_many(s, xs):
    return (lambda y: s(y) and (not y in xs))

def remove_range(s, l, u):
    return (lambda y: s(y) and (y < l or y > u))

def complement(s):
    return (lambda y: not s(y))

def add_one(y):
    return y - 1

def double_it(y):
    return math.sqrt(y)

def map_set(f, s):
    return (lambda y: s(f(y)))

def even(y):
    return  (y % 2) == 0

def filter_set(p, s):
    return (lambda y: p(y) and s(y))

class TestRun(unittest.TestCase):
    def setUp(self):
        self.a = empty_set()
        self.b = singleton(3)
        self.c = range_set(2, 6)
        self.d = range_set(4, 10)

    def test_empty_set(self):
        s = empty_set()
        self.assertEqual(s(5), False)

    def test_singleton(self):
        s = singleton(5)
        self.assertEqual(s(5), True)
        self.assertEqual(s(2), False)

    def test_range_set(self):
        s = range_set(4,10)
        self.assertEqual(s(4), False)
        self.assertEqual(s(5), True)
        self.assertEqual(s(10), False)

    def test_add(self):
        s = add(self.c, 8)
        self.assertEqual(s(8), True)
        self.assertEqual(s(3), True)
        self.assertEqual(s(6), False)

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

    def test_remove(self):
        s = remove(self.d, 7)
        self.assertEqual(s(5), True)
        self.assertEqual(s(7), False)
        self.assertEqual(s(6), True)
        self.assertEqual(s(10), False)

    def test_remove_many(self):
        s = remove_many(self.d, [5,6])
        self.assertEqual(s(5), False)
        self.assertEqual(s(7), True)
        self.assertEqual(s(6), False)
        self.assertEqual(s(10), False)

    def test_remove_range(self):
        s = remove_range(self.d, 7, 9)
        self.assertEqual(s(5), True)
        self.assertEqual(s(8), False)
        self.assertEqual(s(6), True)
        self.assertEqual(s(10), False)

    def test_union(self):
        s = union(self.c, self.d)
        self.assertEqual(s(3), True)
        self.assertEqual(s(2), False)
        self.assertEqual(s(8), True)
        self.assertEqual(s(10), False)

    def test_intersection(self):
        s = intersection(self.c, self.d)
        self.assertEqual(s(3), False)
        self.assertEqual(s(5), True)
        self.assertEqual(s(6), False)
        self.assertEqual(s(8), False)

    def test_complement(self):
        s = complement(self.c)
        self.assertEqual(s(3), False)
        self.assertEqual(s(8), True)
        self.assertEqual(s(6), True)
        self.assertEqual(s(10), True)

    def test_map_set(self):
        s = empty_set()
        t = map_set(add_one, s)
        self.assertEqual(t(6), False)
        self.assertEqual(t(5), False)

        s = singleton(5)
        t = map_set(add_one, s)
        self.assertEqual(t(6), True)
        self.assertEqual(t(5), False)

        s = range_set(3, 9)
        t = map_set(add_one, s)
        self.assertEqual(t(3), False)
        self.assertEqual(t(4), False)
        self.assertEqual(t(5), True)
        self.assertEqual(t(6), True)
        self.assertEqual(t(7), True)
        self.assertEqual(t(9), True)
        self.assertEqual(t(10), False)
        
        t = map_set(double_it, s)
        self.assertEqual(t(3), False)
        self.assertEqual(t(16), True)
        self.assertEqual(t(25), True)
        self.assertEqual(t(36), True)
        self.assertEqual(t(49), True)
        self.assertEqual(t(81), False)
        self.assertEqual(t(100), False)
        

    def test_even(self):
        self.assertEqual(even(3), False)
        self.assertEqual(even(4), True)
        self.assertEqual(even(5), False)

    def test_filter_set(self):
        s = range_set(3, 12)
        t = filter_set(even, s)
        self.assertEqual(t(3), False)
        self.assertEqual(t(4), True)
        self.assertEqual(t(5), False)
        self.assertEqual(t(6), True)
        self.assertEqual(t(7), False)
        self.assertEqual(t(10), True)
        self.assertEqual(t(12), False)

    def teardown(self):
        pass

if __name__ == '__main__':
    unittest.main()
