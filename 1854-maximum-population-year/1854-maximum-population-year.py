class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        logs.sort()
        population = [0 for _ in range(101)]
        
        for start, end in logs:
            birth = start - 1950
            death = end - 1950
            
            population[birth] += 1
            population [death] -= 1
        prefix = 0
        for idx, num in enumerate(population):
            prefix = prefix + num
            population[idx] = prefix
        return population.index(max(population)) + 1950
            
        
        