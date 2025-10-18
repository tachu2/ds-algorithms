import unittest
from hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()

    def test_insert_and_get(self):
        self.ht.insert("key1", "value1")
        self.assertEqual(self.ht.get("key1"), "value1")

        self.ht["key2"] = "value2"
        self.assertEqual(self.ht["key2"], "value2")

    def test_update(self):
        self.ht.insert("key1", "value1")
        self.ht.insert("key1", "value2")
        self.assertEqual(self.ht.get("key1"), "value2")

        self.ht["key1"] = "value3"
        self.assertEqual(self.ht["key1"], "value3")

    def test_remove(self):
        self.ht.insert("key1", "value1")
        self.ht.insert("key2", "value2")
        self.ht.remove("key2")
        self.assertIsNone(self.ht.get("key2"))

        self.ht["key3"] = "value3"
        del self.ht["key3"]
        self.assertIsNone(self.ht.get("key3"))

        self.assertEqual(self.ht["key1"], "value1")

    def test_missing_key(self):
        self.assertIsNone(self.ht.get("not_exist"))

    def test_multiple_items(self):
        for i in range(10):
            self.ht.insert(f"key{i}", i)
        for i in range(10):
            self.assertEqual(self.ht.get(f"key{i}"), i)

    def test_complex_operations(self):
        # Insert keys
        for i in range(100):
            self.ht.insert(f"key{i}", i)
        # Remove even keys
        for i in range(0, 100, 2):
            self.ht.remove(f"key{i}")
        # Re-insert some removed keys with new values
        for i in range(0, 100, 4):
            self.ht.insert(f"key{i}", i * 10)
        # Check values
        for i in range(100):
            if i % 4 == 0:
                self.assertEqual(self.ht.get(f"key{i}"), i * 10)
            elif i % 2 == 0:
                self.assertIsNone(self.ht.get(f"key{i}"))
            else:
                self.assertEqual(self.ht.get(f"key{i}"), i)

    def test_large_number_of_keys(self):
        # Insert a large number of keys
        for i in range(10000):
            self.ht.insert(f"large_key{i}", i)
        # Check retrieval
        for i in range(10000):
            self.assertEqual(self.ht.get(f"large_key{i}"), i)
        # Remove half
        for i in range(0, 10000, 2):
            self.ht.remove(f"large_key{i}")
        # Check removal and existence
        for i in range(10000):
            if i % 2 == 0:
                self.assertIsNone(self.ht.get(f"large_key{i}"))
            else:
                self.assertEqual(self.ht.get(f"large_key{i}"), i)


if __name__ == "__main__":
    unittest.main()
