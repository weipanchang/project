#!/usr/bin/env python
import unittest

class fixedSizeArray(object):
    def __init__(self, arraySize):
        self.arraySize = arraySize
        self.array = [None] * self.arraySize

    def __repr__(self):
        return str(self.array)
    
    def __get__(self, instance, owner):
        return self.array
    
    def __getitem__(self, index):
        try:
            return self.array[index]
        except:
            return 'invalid Index or Array Size Exceeded'

            
    
    def __setitem__(self, index, value):
        self.array = self.array[:index:] + (value,) + self.array[index+1::]

    def append(self, index=None, value=None):
        print "Append Operation cannot be performed on fixed size array"
        return

    def insert(self, index=None, value=None):
        if not index and index - 1 not in xrange(self.arraySize):
            return 'invalid Index or Array Size Exceeded'

        try:
            self.array[index] = value
        except:
            return 'This is Fixed Size Array: Please Use the available Indices'

def store(array, i, v):
    array.insert(i, v)


class TestRun(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_create_array(self):
        my_array_1 = fixedSizeArray(8)
        self.assertEqual((my_array_1[:]), [None, None, None, None, None, None, None, None])
        my_array_2 = fixedSizeArray(0)
        self.assertEqual((my_array_2[:]), [])

    def test_set_value(self):
        my_array_1 = fixedSizeArray(8)
        store(my_array_1, 5, 10)
        self.assertEqual((my_array_1[:]), [None, None, None, None, None, 10, None, None])
        store(my_array_1, 3, "New Value")
        self.assertEqual((my_array_1[:]), [None, None, None, "New Value", None, 10, None, None])
        store(my_array_1, 8, "100")
        self.assertEqual((my_array_1[:]), [None, None, None, "New Value", None, 10, None, None])

    def test_get_value(self):
        my_array_1 = fixedSizeArray(8)
        store(my_array_1, 5, 10)
        store(my_array_1, 3, "New Value")
        self.assertEqual((my_array_1[5]), 10)
        self.assertEqual((my_array_1[3]), "New Value")
        self.assertEqual((my_array_1[8]), 'invalid Index or Array Size Exceeded')
                
    def teardown(self):
        pass


if __name__ == '__main__':
    unittest.main()

