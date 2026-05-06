from Solution import Solutions

n: int = int(input("Enter the disks: "))

solver = Solutions()

solver.towerOfHanoi(n, 'A', 'C', 'B')