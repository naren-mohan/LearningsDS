class Bucket:
    def __init__(self):
        self.bucket = []
    
    def add(self, key):
        if key in self.bucket:
            return
        else:
            self.bucket.append(key)
    
    def remove(self, key):
        if key in self.bucket:
            self.bucket.remove(key)
            
    def contains(self, key):
        #print(self.bucket)
        if key in self.bucket:
            return True
        else:
            return False
                

class MyHashSet:

    def __init__(self):
        #self.hashset = [None] * 1000001 #without bucket implementation
        
        '''self.bucketsize = 1000                                  #N value = 1000
        self.hashset = [[None] * self.bucketsize] * 1001        #1001 buckets implementation
        '''    
        self.hashset = [Bucket()] * 1001
        
    #Totally we create 1000*1001 space for every HashSet
    #Let us consider first three digits for bucket mapping in the hashfunc

    def add(self, key: int) -> None:
        hashval = self.hashfunc(key)
        self.hashset[hashval].add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            hashval = self.hashfunc(key)
            self.hashset[hashval].remove(key)
    
    def hashfunc(self, key: int) -> int:
        hashval = key % 1000
        return hashval
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashval = self.hashfunc(key)
        return self.hashset[hashval].contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
