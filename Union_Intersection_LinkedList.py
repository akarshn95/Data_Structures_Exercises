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
    elements=set()
    linkList=LinkedList()
    
    node=llist_1.head
    while node:
        elements.add(node.value)
        node=node.next
        
    node=llist_2.head
    while node:
        elements.add(node.value)
        node=node.next
    
    for i in elements:
        linkList.append(i)
    
    return linkList
    
def intersection(llist_1, llist_2):
    linkList=LinkedList()
    elements_1=dict()
    elements_2=dict()

    node=llist_1.head
    while node:
        elements_1[node.value]=elements_1.get(node.value,0)+1
        node=node.next
        
    node=llist_2.head
    while node:
        elements_2[node.value]=elements_2.get(node.value,0)+1
        node=node.next
    
    for key in elements_1:
        if key in elements_2:
            linkList.append(key)

    return linkList

# TEST CASES

# Test case 1
print("\nTEST CASE 1\n")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("UNION: ",union(linked_list_1,linked_list_2))
print ("INTERSECTION: ",intersection(linked_list_1,linked_list_2))

# Test case 2
print("\nTEST CASE 2\n")
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("UNION: ",union(linked_list_3,linked_list_4))
print ("INTERSECTION: ",intersection(linked_list_3,linked_list_4))

# Test case 3
print("\nTEST CASE 3\n")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("UNION: ",union(linked_list_1,linked_list_2))
print ("INTERSECTION: ",intersection(linked_list_1,linked_list_2))

# Test case 4
print("\nTEST CASE 4\n")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [9,6,1,2,1,1,1,2,2,2,5,6,7]
element_2 = [1,2,3,4]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("UNION: ",union(linked_list_1,linked_list_2))
print ("INTERSECTION: ",intersection(linked_list_1,linked_list_2))
