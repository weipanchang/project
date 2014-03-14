#!/usr/bin/env python
import unittest
import math

def convert_to_integer(n):
    l = [(ord(i) - ord('0')) for i in n]
    m = [int(math.pow(10, i)) for i in range(len(n) - 1, -1, -1)]
    
    return sum([a * b for a, b in zip(l, m)])

def convert_to_string(n):
    
    m = [int(math.pow(10, i)) for i in range(int(math.log(n, 10)), -1, -1)]
    
    def recursive(n,i):
        if i == len(m) - 1:
            return chr(n + 48)
        else:
            result = chr(n // m[i] + 48)
            n = n % m[i]
        return result + recursive(n, i + 1)
    
    return recursive(n, 0)

class Mytest(unittest.TestCase):
    def setup(self):
        pass
    
    def test_case_1(self):
        self.assertEqual(convert_to_integer('3001'), 3001)
        self.assertEqual(convert_to_integer('1234'), 1234)
        self.assertEqual(convert_to_integer('4'), 4)
    
    def test_case_2(self):
        self.assertEqual(convert_to_string(3001), '3001')
        self.assertEqual(convert_to_string(1234), '1234')
        self.assertEqual(convert_to_string(4), '4')
    
    def teardown(setup):
        pass

if __name__ == '__main__':
    unittest.main()

