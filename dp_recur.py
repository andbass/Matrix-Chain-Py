
import collections as col

def calc_cost(a, b):
    return a[0] * a[1] * b[1]

def calc_size(a, b):
    return [a[0], b[1]]

def multiply(x, y):
    return "({} * {})".format(x, y)

Entry = col.namedtuple("Entry", ("cost", "size", "expr"))
def min_cost(mats, var):
    n = len(mats) + 1
    seen_sequences = [[None] * n for _ in range(n)]

    def min_cost_recur(mats, start, end):
        # Returns (multiplies needed, 
        #          size of resultant matrix, 
        #          expression used to compute)
        if seen_sequences[start][end] is not None:
            return seen_sequences[start][end]

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

        size = calc_size(mats[start], mats[end - 1])

        seen_sequences[start][end] = Entry(
            cost = lowest_cost,
            size = size,
            expr = lowest_expr
        )

        return lowest_cost, size, lowest_expr

    min_cost_recur.count = 0 
    lowest_cost, _, lowest_expr = min_cost_recur(mats, 0, len(mats))

    return lowest_cost, lowest_expr, min_cost_recur.count
