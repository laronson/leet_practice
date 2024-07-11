'''
This problem asks us to create a least recently use cache.  A LRU cache is a caching structure that stores key value 
pairs and also keeps track of which key value pairs have been least recently used (and transitively also most recently 
used).  The LRU cache uses the least recently used information at the point the cache has reached capacity to determine 
which value should be evicted from the cache.  The value that has been used least recently will be the value that is 
evicted.  To accomplish this task, we must create an LRUCache class which accepts a capacity value for the max size of 
the cache and contains two public methods: get and put.  The get method is responsible for getting values by key from 
the cache and then updating that value to be the most recently used value in the cache.  The put method is responsible 
for adding values to the cache (as the most recently used value) and then evicting the least recently used value if the 
new value has pushed the size of the cache over its capacity.

The class we will create contains two data structures: 
1) A doubly linked list that will be used to store the usage information for all key value pairs in the cache.  The list
 will be ordered from most recently used at the heead to least recently used at the rear.  The list will also contain 
 two dummy nodes the head and the rear so as we mutate the list by adding and removing values, the head and rear of the 
 list will always remain as valid nodes.
2) A dictionary to store key value pairs where the key is the user provided key, and the value is a node in the linked 
 list for that key. 

We use a doubly linked list here because it allows us to insert nodes at the head AND remove nodes from the rear of the 
list in O(1) time.  If we want to add a node to the head of the list, we simply set head.next and head.next.prev to be 
the new node, and the new node’s next and prev values to be the head and head.next respectively.  Alternatively, to 
remove a value from the rear of the list, we set rear.prev and rear.prev.next to each other in order to remove the node 
in the middle.  This allows us to quickly add a most recently used node to the front of the list and remove a least 
recently use node from the rear in constant time.

When getting a value from the cache, we first check to make sure that a value exists in the cache for that key.  If it 
dose not we immediately return -1 as the value does not exist.  If the value does exist, we get the node from our 
dictionary, remove the node from our linked list and then re-insert that node at the front of the list to indicate that 
this value is the most recently used value in our cache.  We finally return the existing value from the function.

When putting a value into the cache.  We first check to see if the value already exists in the cache.  If it does, we 
must remove it from the cache before re-inserting with the updated value.  We then create a new node with the 
new/updated key value pair, and then insert that new node at the front of the linked list.  If this new value pushes the
size of the cache over capacity, we get the value at the rear of the list and then remove that value from the list.  
We would then also delete that value from the dictionary of nodes.
'''

class Node:
    def __init__(self, key, val):
        self.key, self.value = key, val
        self.prev = self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.rear = Node(-1,-1), Node(-1,-1)
        self.head.next, self.rear.prev = self.rear, self.head

    def insert(self, node):
        prev, next = self.head, self.head.next
        prev.next = next.prev = node
        node.prev, node.next = prev, next
        

    def remove(self, node):
        next, prev = node.next, node.prev
        prev.next, next.prev = next, prev        
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
            

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.rear.prev
            self.remove(lru)
            self.cache.pop(lru.key, None)

        
