class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    totalSet = set()

    cNode = llist_1.head

    while (cNode):
        totalSet.add(cNode.value)
        cNode = cNode.next

    cNode = llist_2.head

    while (cNode):
        totalSet.add(cNode.value)
        cNode = cNode.next

    returnList = LinkedList()
    
    for item in totalSet:
        returnList.append(item)

    return returnList
    
    

def intersection(llist_1, llist_2):
    # Your Solution Here
    set1 = set()
    set2 = set()

    cNode = llist_1.head

    while (cNode):
        set1.add(cNode.value)
        cNode = cNode.next

    cNode = llist_2.head

    while (cNode):
        set2.add(cNode.value)
        cNode = cNode.next

    intersectingSet = set1 & set2

    returnList = LinkedList()
    
    for item in intersectingSet:
        returnList.append(item)

    return returnList


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = ""

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))
