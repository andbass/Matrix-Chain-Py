
def calc_cost(a, b):
    return a[0] * a[1] * b[1]

def calc_size(a, b):
    return [a[0], b[1]]

def multiply(x, y):
    return "({} * {})".format(x, y)

def min_cost(mats, var):
    def min_cost_recur(mats, start, end):
        # Returns (multiplies needed, 
        #          size of resultant matrix, 
        #          expression used to compute)
        min_cost_recur.count += 1
        seq = mats[start:end]

        if len(seq) == 2:
            return (calc_cost(seq[0], seq[1]),
                    calc_size(seq[0], seq[1]),
                    multiply(var[start], var[end - 1]))
        elif len(seq) == 1:
            return (0, seq[0], var[start])

        lowest_cost = float('inf')
        lowest_expr = None

        for i in range(start, end - 1):
            lcost, lsize, lexpr = min_cost_recur(mats, start, i + 1)
            rcost, rsize, rexpr = min_cost_recur(mats, i + 1, end)

            cost = calc_cost(lsize, rsize)
            total_cost = lcost + cost + rcost

            if total_cost < lowest_cost:
                lowest_cost = total_cost
                lowest_expr = multiply(lexpr, rexpr)

        return (lowest_cost, 
                calc_size(mats[start], mats[end - 1]), 
                lowest_expr)

    min_cost_recur.count = 0 
    lowest_cost, _, lowest_expr = min_cost_recur(mats, 0, len(mats))

    return lowest_cost, lowest_expr, min_cost_recur.count
