class Node(object):
    def __init__(self, k, v):
        self.next = None
        self.pre = None
        self.k = k
        self.v = v


class DLList(object):
    def __init__(self):
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    def insert_after(self, n1, n2):
        assert n1 and n2
        n3 = n1.next
        # update pointers
        n1.next = n2
        n2.pre = n1
        n2.next = n3
        n3.pre = n2

    def remove(self, node):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        node.pre, node.next = None, None

    def move_to_end(self, node):
        self.remove(node)
        self.insert_after(self.tail.pre, node)

    def add_to_end(self, node):
        self.insert_after(self.tail.pre, node)

    def remove_from_head(self):
        delete = self.head.next
        self.remove(delete)
        return delete.k


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = dict()
        self.dll = DLList()
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.map.get(key)
        if not node:
            return -1
        self.dll.move_to_end(node)
        return node.v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.map.get(key)
        if not node:
            node = Node(key, value)
            if self.size + 1 > self.capacity:
                delete_key = self.dll.remove_from_head()
                del self.map[delete_key]
            else:
                self.size += 1
            self.dll.add_to_end(node)
        else:
            node.v = value
            self.dll.move_to_end(node)
        self.map[key] = node
