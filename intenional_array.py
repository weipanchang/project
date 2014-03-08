#!/usr/bin/env python

import unittest

def alloc(n):
    return (lambda x: None if 0 <= x < n else 'invalid Index or Array Size Exceeded')

def store(arr, i, v):
        if arr(i) != 'invalid Index or Array Size Exceeded':
            return (lambda x: v if x == i else arr(x))
        else: return arr

class TestRun(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_create_array(self):
        my_array_1 = alloc(5)
        self.assertEqual(my_array_1(1), None)
        self.assertEqual(my_array_1(6), 'invalid Index or Array Size Exceeded')
        self.assertEqual(my_array_1(-1), 'invalid Index or Array Size Exceeded')
    
    def test_copy_array(self):
        my_array_1 = alloc(5)
        my_array_2 = my_array_1
        self.assertEqual(my_array_2(1), None)
        self.assertEqual(my_array_2(6), 'invalid Index or Array Size Exceeded')
        self.assertEqual(my_array_2(-1), 'invalid Index or Array Size Exceeded')
        
    def test_store(self):
        my_array_1 = alloc(5)
        my_array_2 = store(my_array_1, 2, 10)
        self.assertEqual(my_array_2(1), None)
        self.assertEqual(my_array_2(2), 10)
        self.assertEqual(my_array_2(6), 'invalid Index or Array Size Exceeded')
        
        a = alloc(3)
        a2 = store(a, 10, "hello")
        self.assertEqual(a2(10), 'invalid Index or Array Size Exceeded') 
        

    def teardown(self):
        pass

if __name__ == '__main__':
    unittest.main()
