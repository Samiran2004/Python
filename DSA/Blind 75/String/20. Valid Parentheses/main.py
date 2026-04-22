from BruteForce import BruteForceSolution

s: str = str(input("Enter the parentheses: "))

result = BruteForceSolution()
print(f"{s} is a valid parentheses(Brute Force): {result.isValid(s=s)}")