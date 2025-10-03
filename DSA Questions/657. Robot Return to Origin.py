def judgeCircle(moves: str)-> bool:
    # start = [0, 0]
    # move = {
    #     "U": 1,
    #     "D": -1,
    #     "R": 1,
    #     "L": -1
    # }

    # for i in moves:
    #     if i == "D" or i == "L":
    #         start[0] += move[i]
    #     if i == "U" or i == "R":
    #         start[1] += move[i]
    # return start == [0, 0]

    return moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L')

moves = str(input("Enter the moves: "))
print(judgeCircle(moves=moves))
