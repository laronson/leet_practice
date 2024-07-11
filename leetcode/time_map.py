'''
This problem asks us to build a TimeMap storage class that stores key value pairs.  The TimeMap stores the most recently 
updated value of each key along with the timestamp at which it was created or updated.  The Timemap also stores previous 
updates for each key along with the timestamp those updates were made.

The storage method of this class will be a dictionary where the key for each key-value pair we are going to store will 
act as the key.  The values of each key-value pair in the dictionary will be a list containing tuples which hold the 
value of each update made to that key along with the timestamp that update was made.  The outline of the data structure 
will look something like this:
{key: [(timestamp, value)…]}

The set method will be an O(1) insert into the map.  We will first check if the key exists in the map.  If it does, we 
can simply append the new key update to the list wihin the map.  We can do this safely because we know that calls to set 
will come in order of increasing timestamps so we will not need to search and properly insert an update made at a 
timestamp that happened before the key’s most recent update.  If the key does not exist in the map, we can simply create 
a new entry in the map for that key with an array containing the timestamp and value of the first update.

The get method will first check to see if the key we are looking for exists in the map.  If it does not, then we 
immediately return an empty array.  If the key does exist, we perform a binary search within the list of updates for 
that key for the timestamp that we are looking for.  The logic for our binary search will be as follows:  If the mid of 
our search is greater than the timestamp, then we can set the right pointer to mid-1 because we can only search for 
updates made before or equal to the timestamp passed to the get function.  If the mid of our search is less than or 
equal to the timestamp, we set a result variable to the value at that timestamp and then set the left pointer to mid+1 
and continue our search.  We do this because if a value exists at a more recent timestamp, then our result variable will 
update when that value is reached in the search.  If it does not, then we have already stored the most recent value in 
the values array and can return that as the result of the search.
'''

class TimeMap:

    def __init__(self):
        self.t_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.t_map:
            self.t_map[key].append((timestamp,value))
        else: 
            self.t_map[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.t_map:
            return ""

        values = self.t_map[key]
        l,r,res = 0, len(values)-1, ""
        while l<=r:
            mid = (r + l)//2
            if values[mid][0] <= timestamp:
                # You can save the value here and continue the search
                # May be more effiecnent to break this <= case up and break if timestamp is equal to the current value 
                # to reduce iterations in best case
                res =  values[mid][1]
                l = mid + 1
            elif values[mid][0]> timestamp:
                #Make sure to remember to set l and r to mid +/- 1 to avoid re-searching the mid value in the next
                #search window
                r = mid - 1
        
        return res
