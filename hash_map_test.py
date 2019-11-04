import unittest
import hash_map


class HashMapTest(unittest.TestCase):
    def test_create_with_capacity(self):
        obj = hash_map.HashMap(25)

        self.assertEqual(obj.capacity, 25)
        self.assertEqual(obj.size, 0)

    def test_create_with_default_capacity(self):
        obj = hash_map.HashMap()

        self.assertEqual(obj.capacity, 500)
        self.assertEqual(obj.size, 0)

    def test_set_and_get(self):
        obj = hash_map.HashMap()
        obj.set('a', 15)

        self.assertEqual(obj.get('a'), 15)

    def test_overwrite_same_key(self):
        obj = hash_map.HashMap(10)
        obj.set('a', 15)
        self.assertEqual(obj.get('a'), 15)

        obj.set('a', 25)
        self.assertEqual(obj.get('a'), 25)

    def test_bad_get(self):
        obj = hash_map.HashMap(10)
        obj.set('b', 25)

        self.assertRaises(KeyError, obj.get, 'c')

    def test_delete(self):
        obj = hash_map.HashMap(10)
        obj.set('c', 15)
        obj.set('d', 25)
        deleted = obj.delete('c')

        self.assertRaises(KeyError, obj.get, 'c')
        self.assertEqual(deleted, ('c', 15))
        self.assertEqual(obj.get('d'), 25)

    def test_bad_delete(self):
        obj = hash_map.HashMap(10)
        obj.set('e', 30)

        self.assertRaises(KeyError, obj.delete, 'w')
        self.assertEqual(obj.get('e'), 30)

    def test_set_with_number_key(self):
        obj = hash_map.HashMap()
        obj.set(5, 'test')

        self.assertEqual(obj.get(5), 'test')

    def test_set_with_string_key(self):
        obj = hash_map.HashMap()
        obj.set('test', 25)

        self.assertEqual(obj.get('test'), 25)

    def test_hash_map_resize_up(self):
        obj = hash_map.HashMap(10)
        self.assertEqual(obj.capacity, 10)
        self.assertEqual(obj.size, 0)

        for index in range(15):
            obj.set(index, 'test' + str(index))

        self.assertGreater(obj.capacity, 10)
        self.assertEqual(obj.size, 15)
        self.assertEqual(obj.get(14), 'test14')

    def test_set_large_data_set(self):
        obj = hash_map.HashMap()
        self.assertEqual(obj.capacity, 500)
        self.assertEqual(obj.size, 0)

        for index in range(1000):
            obj.set(index, 'test' + str(index))

        self.assertGreater(obj.capacity, 500)
        self.assertEqual(obj.size, 1000)
        self.assertEqual(obj.get(999), 'test999')


if __name__ == '__main__':
    unittest.main(verbosity=2)
