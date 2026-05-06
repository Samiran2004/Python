class Solutions:
    def towerOfHanoi(self, n, fromm, to, aux):
        if n == 0:
            return
        self.towerOfHanoi(n-1, fromm, aux, to)
        print(f"Disk {n}, moved from {fromm} to {to}")
        self.towerOfHanoi(n-1, aux, to, fromm)