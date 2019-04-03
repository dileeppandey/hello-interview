class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = 0
        self.MAX_SIZE = k
        self.items = [0] * self.MAX_SIZE
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.size == self.MAX_SIZE:
            return False
        else:
            if self.rear == -1:
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.MAX_SIZE
            self.items[self.rear] = value
            self.size += 1
            return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        if self.rear == self.front:
            self.rear = self.front = -1
        else:
            self.front = (self.front + 1) % self.MAX_SIZE
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.items[self.front] if self.size != 0 else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.items[self.rear] if self.size != 0 else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.MAX_SIZE


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
