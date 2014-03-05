#!/usr/bin/env python
import unittest

def empty_set():
    return (lambda x: False)

def singleton(x):
    return (lambda y: y ==x)
def ranger(a, b):
    return (lambda x: x > a and x < b)


class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_empty_set(self):
        s = empty_set()
        self.assertEqual(s(5), False)

    def singleton(self):
        s = singleton(5)
        self.assertEqual(s(5), True)
        self.assertEqual(s(2), False)
        
    def test_empty_set(self):
        s = ranger(4,10)
        self.assertEqual(s(5), True)
        self.assertEqual(s(2), False)
        self.assertEqual(s(12), False)
    def teardown(self):
        pass
 
if __name__ == '__main__':
    unittest.main()
