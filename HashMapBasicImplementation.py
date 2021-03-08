class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.hashmap = [-1] * 1000001
        
        

    def put(self, key: int, value: int) -> None:
        hashval = self.hashfunc(key)
        self.hashmap[hashval] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashval = self.hashfunc(key)
        return self.hashmap[hashval]
             

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashval = self.hashfunc(key)
        self.hashmap[hashval] = -1
        
    def hashfunc(self, key):
        hashval = key 
        return hashval


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
