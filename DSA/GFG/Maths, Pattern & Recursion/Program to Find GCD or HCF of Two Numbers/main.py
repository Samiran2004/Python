from UsingLoopApproach import UsingLoopSolution
from UsingEuclideanAlgorithmApproach import Solution
from UsingOptimizedEuclideanAlgorithmApproach import Solution as OptimizeSolution

a: int = int(input("Enter the value of first number: "))
b: int = int(input("Enter the value of second number: "))

result = UsingLoopSolution().gcd(a, b)
print(f"The value of GCD of {a}, {b} is {result}")

result = Solution().gcd(a, b)
print(f"The value of GCD if {a}, {b} using Eucildean Algorithm is {result}")

result = OptimizeSolution().gcd(a, b)
print(f"The value of GCD if {a}, {b} using Optimized Eucildean Algorithm is {result}")