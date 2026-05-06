class BruteForceSolution:
    def josephus(self, n, k):
        def josRec(person, k, index):
            if len(person) == 1:
                return person[0]
            index = (index + k - 1) % len(person)

            person.pop(index)

            return josRec(person, k, index)

        index = 0
        person = []
        for i in range(1, n+1):
            person.append(i)

        return josRec(person, k, index)