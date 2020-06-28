def CheckWin(x, won, subset=[]):
    # magic square: all diagonals horizontals and verticals sum to equal 15, no other sum of 3 ints within the square equal 15, so if 3 ints x currently holds sum to 15, x has won
    if len(subset) == 3:
        total = sum(subset)
        if total == 15:
            won = True
            return won

    for i in range(len(x)):
        n = x[i]
        remaining = x[i+1:]
        won = CheckWin(remaining, won, subset + [n])
        if won:
            break
    return won