class BruteForceSolution:
    def sumOfNaturals(self, n: int):
        sum = 0
        i = 1
        
        while i <= n:
            sum += i
            i += 1
        return sum