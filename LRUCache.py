class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, doubleNode):
        if self.head is None:
            self.head = doubleNode
            self.tail = self.head
            return
            
        self.tail.next = doubleNode
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

    def prepend(self, doubleNode):
        if self.head is None:
            self.head = doubleNode
            self.tail = self.head
            return

        doubleNode.next = self.head    
        self.head.previous = doubleNode
        self.head = self.head.previous
        return

    def pop(self):
        if self.tail is None:
            return None
        else:
            returnValue = self.tail
            if self.tail.previous is not None:
                self.tail.previous.next = None
                self.tail = self.tail.previous
            else:
                self.tail = None
                self.head = None
            return returnValue

    def moveToFront(self, doubleNode):
        if doubleNode.previous == None:
            return
        else:
            doubleNode.previous.next = doubleNode.next
            if doubleNode.next:
                doubleNode.next.previous = doubleNode.previous
            doubleNode.previous = None
            doubleNode.next = self.head
            self.head = doubleNode
            return         

class LRU_Cache_Item():
    def __init__(self, key, value):
        self.key = key
        self.val = value

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.keyList = DoublyLinkedList()
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if (key in self.cache and self.cache[key] != None):
            self.keyList.moveToFront(self.cache[key])
            return self.cache[key].value.val
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if (key in self.cache):
            self.cache[key].value.val = value
            self.keyList.moveToFront(self.cache[key])
        else:
            newItem = LRU_Cache_Item(key, value)
            newNode = DoubleNode(newItem)
            self.cache[key] = newNode
            self.keyList.prepend(newNode)
            if self.capacity == self.size:
                poppedKey = self.keyList.pop()
                self.cache[poppedKey.value.key] = None
            else:
                self.size+=1
        
        return

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(3))       # return -1
print(our_cache.get(4))       # return 4
print(our_cache.get(5))       # return 5
print(our_cache.get(6))       # return 6
our_cache.set(7,7)
print(our_cache.get(1))       # return -1 as was last retrieved/set item

our_cache.set('my key', {'a nested object': 'works'})
print(our_cache.get('my key')) #should return {'a nested object': 'works'}
print(our_cache.get(2)) #should return -1