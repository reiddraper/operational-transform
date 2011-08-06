#!/usr/bin/env python

import unittest

import transform

class TestTransform(unittest.TestCase):
    def setUp(self):
        pass

    def test_insert_insert_1(self):
        o1 = transform.insert_helper(0, 'z')
        o2 = transform.insert_helper(3, 'x')

        expected = transform.insert_helper(4, 'x')
        received = transform.transform(o2, o1)

        self.assertEqual(expected, received)

    def test_insert_insert_2(self):
        o1 = transform.insert_helper(3, 'z')
        o2 = transform.insert_helper(3, 'x')

        expected = transform.insert_helper(4, 'x')
        received = transform.transform(o2, o1)

        self.assertEqual(expected, received)

    def test_insert_insert_3(self):
        o1 = transform.insert_helper(3, 'z')
        o2 = transform.insert_helper(3, 'z')

        expected = None 
        received = transform.transform(o2, o1)

        self.assertEqual(expected, received)

    def test_insert_insert_4(self):
        o1 = transform.insert_helper(10, 'z')
        o2 = transform.insert_helper(3, 'x')

        expected = o2 
        received = transform.transform(o2, o1)

        self.assertEqual(expected, received)

    def test_insert_insert_5(self):
        o1 = transform.insert_helper(0, 'z')
        o2 = transform.insert_helper(0, 'x')

        expected = transform.insert_helper(1, 'x') 
        received = transform.transform(o2, o1)

        self.assertEqual(expected, received)

    def test_delete_insert_1(self):
        o1 = transform.insert_helper(3, 'z')
        o2 = transform.delete_helper(0)
        
        expected = o2
        received = transform.transform(o2, o1)

        self.assertEqual(expected, received)

    def test_delete_insert_2(self):
        o1 = transform.insert_helper(3, 'z')
        o2 = transform.delete_helper(3)
        
        expected = transform.delete_helper(4)
        received = transform.transform(o2, o1)

        self.assertEqual(expected, received)

    def test_insert_delete_1(self):
        o1 = transform.delete_helper(3)
        o2 = transform.insert_helper(0, 'x')
        
        expected = o2
        received = transform.transform(o2, o1)

        self.assertEqual(expected, received)

    def test_insert_delete_2(self):
        o1 = transform.delete_helper(0)
        o2 = transform.insert_helper(10, 'x')
        
        expected = transform.insert_helper(9, 'x')
        received = transform.transform(o2, o1)

        self.assertEqual(expected, received)

    def test_delete_delete_1(self):
        o1 = transform.delete_helper(0)
        o2 = transform.delete_helper(0)
        
        expected = None 
        received = transform.transform(o2, o1)

        self.assertEqual(expected, received)

    def test_delete_delete_2(self):
        o1 = transform.delete_helper(0)
        o2 = transform.delete_helper(5)
        
        expected = transform.delete_helper(4)
        received = transform.transform(o2, o1)

        self.assertEqual(expected, received)

    def test_multiple_transform_1(self):
        o1 = transform.delete_helper(0)
        o2 = transform.insert_helper(5, 'z')
        o3 = transform.insert_helper(10, 'x')

        expected = o3
        received = transform.transform_many(o3, [o1, o2])

        self.assertEqual(expected, received)

    def test_multiple_transform_2(self):
        o1 = transform.insert_helper(1, 'x')
        o2 = transform.insert_helper(2, 'y')
        o3 = transform.insert_helper(3, 'z')

        expected = transform.insert_helper(5, 'z')
        received = transform.transform_many(o3, [o1, o2])

        self.assertEqual(expected, received)

    def test_multiple_transform_3(self):
        o1 = transform.delete_helper(10)
        o2 = transform.delete_helper(2)
        o3 = transform.delete_helper(1)
        o4 = transform.delete_helper(5)

        expected = transform.delete_helper(3)
        received = transform.transform_many(o4, [o1, o2, o3])

        self.assertEqual(expected, received)

    def test_multiple_transform_4(self):
        o1 = transform.insert_helper(4, 'x')
        o2 = transform.delete_helper(7)

        expected = transform.delete_helper(8)
        received = transform.transform_many(o2, [o1])

        self.assertEqual(expected, received)

    def test_multiple_transform_5(self):
        o1 = transform.insert_helper(4, 'x')
        o2 = transform.delete_helper(7)
        o3 = transform.insert_helper(4, 'x')

        expected = None 
        received = transform.transform_many(o3, [o1, o2])

        self.assertEqual(expected, received)

    def test_multiple_transform_6(self):
        o1 = transform.delete_helper(4)
        o2 = transform.delete_helper(7)
        o3 = transform.delete_helper(4)

        expected = None 
        received = transform.transform_many(o3, [o1, o2])

        self.assertEqual(expected, received)
       
    def test_multiple_transform_7(self):
        updates = [{u'index': 3, u'type': u'delete'}, {u'index': 2, u'type': u'insert', u'item': u'Shadows on parade'}]
        to_transform = [{u'index': 0, u'type': u'delete'}, {u'index': 1, u'type': u'insert', u'item': u'Galaxies'}]
        result = [transform.transform_many(up, to_transform) for up in updates]
        expected = [{'index': 3, 'type': 'delete'}, 
        {'index': 2, 'type': 'insert', 'item': u'Shadows on parade'}]

    def test_multiple_transform_8(self):
        o1 = transform.delete_helper(0)
        o2 = transform.insert_helper(1, "Gettin' Up")
        o3 = transform.insert_helper(0, 'Galaxies')

        expected = o3 
        received = transform.transform_many(o3, [o1, o2])

        self.assertEqual(expected, received)

    def test_multiple_transform_9(self):
        o1 = transform.delete_helper(0)
        o2 = transform.delete_helper(0)
        o3 = transform.delete_helper(0)

        expected = None 
        received = transform.transform_many(o3, [o1, o2])

        self.assertEqual(expected, received)

if __name__ == '__main__':
    unittest.main()
        
