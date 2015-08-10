import unittest

from nose.tools import istest

from data_structures.disjoint_set import DisjointSet


class DisjointSetTest(unittest.TestCase):


    def setUp(self):
        self.ds = DisjointSet()

    @istest
    def add_elements(self):
        self.ds.add(1)
        self.assertEquals(1, len(self.ds))
        self.ds.add('a')
        self.assertEquals(2, len(self.ds))

    @istest
    def add_many_elements(self):
        self.ds.add_many([1, 2, 3])
        self.assertEquals(3, len(self.ds))
        self.ds.add_many(letter for letter in 'abc')
        self.assertEquals(6, len(self.ds))

    @istest
    def find_set_representitive(self):
        test_elements = [1, 2, 3]
        self.ds.add_many(test_elements)
        for element in test_elements:
            self.assertEquals(element, self.ds.find(element))
