import unittest
from hypothesis import given
import hypothesis.strategies as st
from Hash import *


class TestMutableHashMap(unittest.TestCase):
    def setUp(self):
        self.hashMap = Hash()


class TestMutableHashMapMethods(TestMutableHashMap):
    def test_init(self):
        self.assertEqual(self.hashMap.len, 5)
        self.assertIsInstance(self.hashMap.data, list)
        self.assertEqual(self.hashMap.data[0], [])
        self.assertEqual(self.hashMap.data[1], [])
        self.assertEqual(self.hashMap.data[2], [])
        self.assertEqual(self.hashMap.data[3], [])
        self.assertEqual(self.hashMap.data[4], [])

    def test_put(self):
        for i in range(5):
            self.hashMap.put(i)
        self.assertEqual(self.hashMap.data[0], [0])
        self.assertEqual(self.hashMap.data[1], [1])
        self.assertEqual(self.hashMap.data[2], [2])
        self.assertEqual(self.hashMap.data[3], [3])
        self.assertEqual(self.hashMap.data[4], [4])
        self.assertEqual(self.hashMap.put("String"), False)

    def test_remove(self):
        self.hashMap.put(0)
        self.assertEqual(self.hashMap.data[0], [0])
        self.hashMap.remove(0)
        self.assertEqual(self.hashMap.data[0], [])
        self.assertEqual(self.hashMap.remove("String"), False)

    def test_size(self):
        self.assertEqual(self.hashMap.size(), 5)

    def test_key_num(self):
        self.assertEqual(self.hashMap.key_number(), 0)

    def test_from_list(self):
        list_a = [0, 1, 2, 3, 4, 11]
        self.hashMap.from_list(list_a)
        self.assertEqual(self.hashMap.data[0], [0])
        self.assertEqual(self.hashMap.data[1], [1, 11])
        self.assertEqual(self.hashMap.data[2], [2])
        self.assertEqual(self.hashMap.data[3], [3])
        self.assertEqual(self.hashMap.data[4], [4])

    def test_is_member(self):
        list_a = [0, 1, 2, 3, 4, 11]
        self.hashMap.from_list(list_a)
        self.assertEqual(self.hashMap.is_member(11), True)
        self.assertEqual(self.hashMap.is_member(9), False)

    def test_filter(self):
        list_a = [0, 1, 2, 3, 4, 11]
        self.hashMap.from_list(list_a)

        def filterOdd(value):
            if value % 2 == 0:
                return True
            else:
                return False

        res = self.hashMap.filter(filterOdd)
        self.assertEqual(res, [0, 2, 4])

    def test_map(self):
        list_a = [0, 1, 2, 3, 4, 11]
        self.hashMap.from_list(list_a)

        def mapPlusOne(value):
            return value + 1

        res = self.hashMap.map(mapPlusOne)
        self.assertEqual(res, [1, 2, 12, 3, 4, 5])

    def test_reduce(self):
        list_a = [0, 1, 2, 3, 4, 11]
        self.hashMap.from_list(list_a)

        def reduceSum(accumulator, curr):
            return accumulator + curr

        res = self.hashMap.hash_reduce(reduceSum, 0)
        self.assertEqual(res, 21)




    ## The property - based tests

    '''
        when a=[5,5]
        b=[5]
        it is not a fault,
        because hashmap does not allow repeat value  
    '''

    @given(st.lists(st.integers(5)))
    def test_from_list_to_list_equality(self, a):
        hash1 = Hash()
        hash1.from_list(a)
        b = hash1.to_list()
        self.assertEqual(a, b)

    '''
    the same reason as above   
    hashmap does not allow repeat value      
    '''

    @given(st.lists(st.integers()))
    def test_python_len_and_list_size_equality(self, a):
        hash1 = Hash()
        hash1.from_list(a)
        self.assertEqual(hash1.key_number(), len(a))

    def test_iter(self):
        x = [1, 2, 3]
        hash1 = Hash()
        hash1.from_list(x)
        tmp = []
        for e in hash1:
            tmp.append(e)
        self.assertEqual(x, tmp)
        self.assertEqual(hash1.to_list(), tmp)
        i = iter(Hash())
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == "__main__":
    unittest.main()
