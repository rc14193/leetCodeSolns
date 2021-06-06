# https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1140/
# According to trial 272ms and 16.9mb
# 49.84% time and 99.19% space

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = []
        for _ in range(80):
            self.store.append([])


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        y = key % 80
        add_pair = (key, value)
        for count, val in enumerate(self.store[y]):
            if val[0] == key:
                self.store[y][count] = add_pair
                return
        self.store[y].append(add_pair)


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        y = key % 80
        for val in self.store[y]:
            if val[0] == key:
                return val[1]
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        y = key % 80
        for count, val in enumerate(self.store[y]):
            if val[0] ==  key:
                self.store[y].pop(count)
                return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
