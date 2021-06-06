# https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1139/
# According to trial 160ms and 18.6mb
# 78.74 % time and 92.01% space

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        for i in range(80):
            self.arr.append([])


    def add(self, key: int) -> None:
        y = key % 80
        not key in self.arr[y] and self.arr[y].append(key)


    def remove(self, key: int) -> None:
        y = key % 80
        key in self.arr[y] and self.arr[y].remove(key)


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        y = key % 80
        return key in self.arr[y]



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
