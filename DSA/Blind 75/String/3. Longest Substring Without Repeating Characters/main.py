from BruteForce import BruteForceSolution
from OptimalApproach import OptimalApproachSolution

s = str(input("Enter the string: "))

result = BruteForceSolution()
print(result.lengthOfLongestSubstring(s=s))

result = OptimalApproachSolution()
print(result.lengthOfLongestSubstring(s=s))