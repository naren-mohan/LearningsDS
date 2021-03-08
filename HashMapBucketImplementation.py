class Bucket:
    def __init__(self):
        self.bucket = []
    
    def put(self, key, val):
        Found = False
        for k,v in self.bucket:
            if k == key:
                self.bucket.remove((k,v))
                self.bucket.append((key,val))
                Found = True
        
        if not Found:
            self.bucket.append((key,val))
    
    def get(self, key):
        Found = False
        for k,v in self.bucket:
            if k == key:
                return v
        
        if not Found:
            return -1
        
    def remove(self, key):
        for k,v in self.bucket:
            if k == key:
                self.bucket.remove((k,v))
                return    

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.hashmap = [Bucket()] * 1001
        
        

    def put(self, key: int, value: int) -> None:
        hashval = self.hashfunc(key)
        self.hashmap[hashval].put(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashval = self.hashfunc(key)
        
        return self.hashmap[hashval].get(key)
             

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashval = self.hashfunc(key)
        self.hashmap[hashval].remove(key)
        
    def hashfunc(self, key):
        hashval = key % 1000
        return hashval


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
