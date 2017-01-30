

def find_odd_int(seq):
    """ Find single int occurring odd number of times """
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


if __name__ == "__main__":
    assert find_odd_int([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
