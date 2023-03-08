class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.maximum = []
        hashmap = {}
        self.track = persons[0]
        
        for person in self.persons:
            hashmap[person] = hashmap.get(person,0) + 1
            if hashmap[person] >= hashmap[self.track]:
                self.track = person
            self.maximum.append(self.track)
        
    def q(self, t: int) -> int:
        left, right  = 0 , len(self.times) - 1
        
        while left <= right:
            middle = (left + right) //2
            
            if self.times[middle] > t:
                right = middle - 1
            else:
                left = middle + 1
        return self.maximum[left - 1]
            
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)