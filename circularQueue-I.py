class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = k * [None]
        self.head = 0
        self.tail = 0
        self.length = k

    def enQueue(self, value: int) -> bool:
        if self.queue[self.tail] is None:
            self.queue[self.tail] = value
            self.tail = (self.tail+1) % self.length
            return True
        return False
                
    def deQueue(self) -> bool:
        if self.queue[self.head] is not None:
            self.queue[self.head] = None
            self.head = (self.head+1) % self.length
            return True
        return False
        

    def Front(self) -> int:
        if self.queue[self.head] is not None:
            return self.queue[self.head]
        return -1

    def Rear(self) -> int:
        if self.queue[(self.tail-1)%self.length] is not None:
            return self.queue[(self.tail-1)%self.length]
        return -1
                

    def isEmpty(self) -> bool:
        if self.head == self.tail:
            if self.queue[self.head] is None:
                return True
        return False
        
    def isFull(self) -> bool:
        if self.head == self.tail:
            if self.queue[self.head] is not None:
                return True
        return False    


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
