class HashTable:
    """
    HashTable implementation using open addressing with linear probing.
    """
    class Entry:
        __slots__ = ("key", "value", "hash")
        def __init__(self, key, value, hash):
            self.key = key
            self.value = value
            self.hash: int = hash

        def __str__(self):
            return f"Node(key={self.key}, value={self.value}, hash={self.hash})"

    NULL = Entry(None, None, -1)  # 空いているスロット
    TOMBSTONE = Entry(None, None, -2)  # 削除されたスロット。ここには挿入しない
    TABLE_MAX_LOAD = 0.75  # 最大保有率。これを超えたらリサイズする

    def __init__(self):
        self.size: int = 0
        self.capacity: int = 8
        self.arr: list[self.Entry] = [self.NULL] * self.capacity

    def _index(self, key_hash: int) -> int:
        return key_hash & (self.capacity - 1)

    def insert(self, key, value):
        if (self.size + 1) / self.capacity >= self.TABLE_MAX_LOAD:
            self._resize()
        key_hash = hash(key)
        index = key_hash % self.capacity

        while True:
            entry = self.arr[index]
            if entry is self.NULL:
                break
            if key_hash == entry.hash and key == entry.key:
                # 既に存在する場合は上書き
                entry.value = value
                return
            # tombstoneもしくはcollasion場合は次のインデックスへ
            index = (index + 1) % self.capacity

        self.arr[index] = self.Entry(key, value, key_hash)
        self.size += 1

    def _find(self, key) -> Entry | None:
        key_hash = hash(key)
        index = key_hash % self.capacity

        while True:
            entry = self.arr[index]
            if entry is self.NULL:
                return None
            if key_hash == entry.hash and key == entry.key:
                return entry
            index = (index + 1) % self.capacity

    def get(self, key):
        entry = self._find(key)
        return entry.value if entry else None

    def remove(self, key) -> bool:
        key_hash = hash(key)
        index = key_hash % self.capacity

        while True:
            entry = self.arr[index]
            if entry is self.NULL:
                return False
            if key_hash == entry.hash and key == entry.key:
                self.arr[index] = self.TOMBSTONE
                return True
            index = (index + 1) % self.capacity

    def _resize(self):
        old_arr = self.arr
        old_capacity = self.capacity
        self.capacity = old_capacity * 2
        self.arr = [self.NULL] * (self.capacity)
        self.size = 0
        for entry in old_arr:
            if entry is self.NULL or entry is self.TOMBSTONE:
                continue
            self.insert(entry.key, entry.value)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.remove(key)

    def __contains__(self, key):
        return self._find(key) is not None

    def __str__(self):
        return str([str(entry) for entry in self.arr])


def main():
    ht = HashTable()
    for i in range(10):
        ht.insert(f"key{i}", f"value{i}")

    print(ht)
    for i in range(20):
        if f"key{i}" in ht:
            print(f"Found: {ht[f'key{i}']}")
        else:
            print(f"Not Found: key{i}")

    for i in range(10):
        ht.insert(f"key{i}", f"value{i * 2}")

    for i in range(20):
        if f"key{i}" in ht:
            entry = ht._find(f"key{i}")
            print(f"Found: {entry}")
        else:
            print(f"Not Found: key{i}")

    for i in range(5):
        del ht[f"key{i}"]

    for i in range(20):
        if f"key{i}" in ht:
            entry = ht._find(f"key{i}")
            print(f"Found: {entry}")
        else:
            print(f"Not Found: key{i}")

    for i in range(1, 10):
        ht.insert(f"key{i * 2}", f"value{i * 3}")

    for i in range(20):
        if f"key{i}" in ht:
            entry = ht._find(f"key{i}")
            print(f"Found: {entry}")
        else:
            print(f"Not Found: key{i}")
    print(ht)


if __name__ == "__main__":
    main()
