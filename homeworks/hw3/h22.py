# x is the intended sum, and vals is a list of the types of change
def ways(x, vals):
    #First, we need our base cases:

    if x < 0:
        return 0
    # We have all the change we need or we just need some pennies
    elif x == 0 or len(vals) == 1:
        return 1

    return ways(x - vals[-1], vals) + ways(x, vals[:-1])
print(ways(31.37, [0.01, 0.05, 0.25, 1.00]))
