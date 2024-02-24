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
