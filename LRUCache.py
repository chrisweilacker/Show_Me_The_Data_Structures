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
        doubleNode.previous = self.tail
        self.tail = self.tail.next
        return

    def prepend(self, doubleNode):
        if self.head is None:
            self.head = doubleNode
            self.tail = self.head
            return

        doubleNode.next = self.head    
        self.head.previous = doubleNode
        self.head = doubleNode
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
            else:
                self.tail = doubleNode.previous
            
            doubleNode.previous = None
            doubleNode.next = self.head
            self.head.previous = doubleNode
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
        if (key in self.cache and self.cache[key]!=None):
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

our_cache.set('mykey', {'a nested object': 'works'})
print(our_cache.get('mykey')) #should return {'a nested object': 'works'}
print(our_cache.get(2)) #should return -1

# capacity at two
our_cache = LRU_Cache(2)

# fill out cache
our_cache.set(1, 'one')  # older
our_cache.set(2, 'two')  # newer

# executed a get, this means item 1 is *more* recently used than item 2.
print(our_cache.get(1))

# add a new item. this should remove item 2 because it is less recently used.
our_cache.set(3, 'three')

# item 1 should still be present
print(our_cache.get(1))

# item 2 should deleted (returns -1)
print(our_cache.get(2))
our_cache.set('', 'one') #works as an empty string can still be a key in a dictionary though not sure why
mydict={'': 'Im an empty key'}
print(mydict[''])

print(our_cache.get(''))


our_cache.set(None, 'one') #Works as None is converted into the string None
print(our_cache.get(None))