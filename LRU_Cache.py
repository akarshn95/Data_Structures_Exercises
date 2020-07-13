class Double_LL(object):
    
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache=dict()
        self.capacity=capacity
        self.head=Double_LL(0,0)
        self.tail=Double_LL(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            self._remove(self.cache[key])
        node=Double_LL(key,value)
        self._add(node)
        self.cache[key]=node
        if len(self.cache)>self.capacity:
            rem_node=self.head.next
            self._remove(rem_node)
            del self.cache[rem_node.key]
                 
    def _remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
    
    def _add(self,node):
        node.next=self.tail
        node.prev=self.tail.prev
        self.tail.prev.next=node
        self.tail.prev=node


# TEST CASES

our_cache = LRU_Cache(5)
print("our_cache")

print(our_cache.get(4) )      #returns -1 because empty cache

our_cache.set(1, 1)   
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))      # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3) )     # returns -1 because the cache reached its capacity and 3 was the least recently used entry


my_cache=LRU_Cache(9)
print("my_cache")

print(my_cache.get(9))    #returns -1 because empty

my_cache.set(1, 11)   
my_cache.set(2, 22)
my_cache.set(3, 33)
my_cache.set(4, 44)
my_cache.set(5, 55)   
my_cache.set(6, 66)
my_cache.set(7, 77)
my_cache.set(8, 88)
my_cache.set(9, 99)
my_cache.set(10, 100)

print(my_cache.get(1))   #returns -1 because it has been cleared for being LRU
print(my_cache.get(10))

the_cache=LRU_Cache(1)
print("the_cache")
print(the_cache.get(1000))          #returns -1

the_cache.set(0,0)
the_cache.set(0,111)

print(the_cache.get(0))         #returns 111 which is the updated value for key 0


