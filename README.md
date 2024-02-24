# DOHD2-Data-Structure

Deletion Oriented Hashmap Deformation (DOHD) is a custom data structure that 
implements a queue using a Python dictionary. It is designed to manage a collection 
of unique objects in a specific order, with the ability to add new objects to the 
end of the queue and remove objects from the front, while keeping track of the 
original position of each object in the queue (adjusted for deletions).

This class is intended for use in scenarios where a queue-like data structure is 
needed, but there is also a need to quickly check the position of items or ensure 
items are unique. It is specifically designed for use within an algorithm that 
controls all inputs and operations, and therefore does not include error handling 
for unexpected inputs or usage.


## Attributes:
    HashMap (dict): A dictionary that stores the objects as keys and their indices as values.
    
    hashDeletions (int): A counter that keeps track of the number of deletions.

## Methods:
    __init__(self, keyArr): Initializes the DOHD with an array of keys.
    
    __hashArrs(self,array): Hashes an array into a dictionary.
    
    getIndex(self,Object): Returns the index of a given object in the original array, adjusted by the number of deletions.
    
    queueHash(self,Object): Adds a new object to the end of the queue.
    
    popHashMap(self): Removes the first object in the queue.
