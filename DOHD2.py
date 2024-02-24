
"""
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


 Attributes:
    HashMap (dict): A dictionary that stores the objects as keys and their indices as values.
    hashDeletions (int): A counter that keeps track of the number of deletions.

 Methods:
    __init__(self, keyArr): Initializes the DOHD with an array of keys.
    __hashArrs(self,array): Hashes an array into a dictionary.
    getIndex(self,Object): Returns the index of a given object in the original array, adjusted by the number of deletions.
    queueHash(self,Object): Adds a new object to the end of the queue.
    popHashMap(self): Removes the first object in the queue.
"""




class DOHD: #Deletion Oriented Hashmap Deformation
    
    def __init__(self, keyArr): 
        self.HashMap = self.__hashArrs(keyArr)
        self.hashDeletions = 0
    
    
    # SC = O(n), TC = O(n)
    def __hashArrs(self,array): #Only ever executes once
        return {x:i for (i,x) in enumerate(array)}
    
    
    # SC = O(1), TC = O(1)
    def getIndex(self,Object):
        return self.HashMap[Object]-self.hashDeletions
        
        
    # SC = O(1), TC = O(1) 
    def queueHash(self,Object):
        if(Object not in self.HashMap): 
            self.HashMap[Object] = next(reversed(self.HashMap.items()))[1]+1
    
    
    # SC = O(1), TC = O(1)
    def popHashMap(self):
        del self.HashMap[next(iter(self.HashMap.keys()))]
        self.hashDeletions += 1