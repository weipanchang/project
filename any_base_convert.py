#!/usr/bin/env python
import unittest

import math

def decimal_to_binary(n, base):
    l = [int(math.pow(base, i)) for i in range(int(math.log(n, base)), -1, -1)]
    def recursive(n, i):
        
        if i ==  len(l)-1:
            return str(n)
        else:
            if n >= l[i]:
                x = str(n // l[i])
                n = n  % l[i]
            else: x = '0'
            return x + (recursive(n, i + 1))

    return recursive(n, 0)

def binary_to_decimal(s, base):
    l = [int(math.pow(base, i)) for i in range(len(s) - 1, -1, -1)]
    m = [int (x) for x in s]
    return sum([a * b for a, b in zip(l, m)])
    #def recursive( i):
    #    if i == len(s) - 1:
    #        return int(s[i]) * int(l[i])
    #    else:
    #        result = int(s[i]) * int(l[i])
    #        return result + recursive( i + 1)
    #return recursive(0)


class TestRun(unittest.TestCase):
    def setup(self):
        pass
    def test_run_1(self):
        self.assertEqual(decimal_to_binary(14,4), '32')
        self.assertEqual(decimal_to_binary(13,2), '1101')
        self.assertEqual(decimal_to_binary(13,5), '23')

    def test_run_2(self):
        self.assertEqual(binary_to_decimal('32', 4), 14)
        self.assertEqual(binary_to_decimal('1101', 2), 13)
        self.assertEqual(binary_to_decimal('23', 5), 13)


    def teardown(self):
        pass

if __name__ == '__main__':
    unittest.main()