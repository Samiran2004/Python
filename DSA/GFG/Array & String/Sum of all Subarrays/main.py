from BruteForceApproach import BruteForceApproachSolution
from BetterApproach import BetterApproachSolution

test_cases = [
    [1, 3],
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 4, 5, 3, 2]
]

i = 1
for test in test_cases:
    result = BruteForceApproachSolution().subarraySum(test)
    if result:
        print(f"Test Case {i} Pass")
        print(f"Result for Test Case: {test} is {result}")
        i += 1
    else:
        print(f"Test Case {i} Failed!")
        print(f"Test Case Input: {test}")
        i += 1

print("\n\n---------------BETTER APPROACH---------------\n")
for test in test_cases:
    result = BetterApproachSolution().subarraySum(test)
    if result:
        print(f"Test Case {i} Pass")
        print(f"Result for Test Case: {test} is {result}")
        i += 1
    else:
        print(f"Test Case {i} Failed!")
        print(f"Test Case Input: {test}")
        i += 1