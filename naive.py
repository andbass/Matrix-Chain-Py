
from matrix import *

def make_expr(terms):
    return "({})".format(" * ".join(terms))

def sequences(terms):
    # A set is used to eliminate redundant combinations
    seqs = set()

    def seq_recur(terms, seqs):
        # Used to identify relative complexity of algorithm
        seq_recur.count += 1

        if len(terms) == 2:
            # If given only two terms, there exists only 1
            # way to multiply them together without reordering operands
            product = "{} * {}".format(terms[0], terms[1])
            seqs.add(product)

            return

        for i in range(len(terms) - 1):
            # Extract out pair of terms to multiply
            pair = terms[i:i + 2]

            # Multiply together paired terms, 
            # and preserve terms that are yet to be touched
            rest = terms[:i] + [make_expr(pair)] + terms[i + 2:]
        
            # Now consider new set of terms, 
            # where paired terms are grouped together
            seq_recur(rest, seqs)

    # Used to identify relative complexity of algorithm
    seq_recur.count = 0
    seq_recur(terms, seqs)

    return seqs, seq_recur.count

def least_ops(sequences, var):
    best_mat = eval(sequences[0], var)
    best_seq = sequences[0]

    for seq in sequences[1:]:
        result = eval(seq, var)
        
        if result.multiplies < best_mat.multiplies:
            best_mat = result
            best_seq = seq

    return best_seq, best_mat
