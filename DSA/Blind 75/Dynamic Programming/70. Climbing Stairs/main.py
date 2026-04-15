from BruteForce import BruteForceSolution
from TopDown import TopDownSolution
from BottomUp import BottomUpSolution

n = int(input("Enter the number: "))

result = BruteForceSolution()
print(result.climbStairs(n=n))

result = TopDownSolution()
print(result.climbStairs(n=n))

result = BottomUpSolution()
print(result.climbStairs(n=n))