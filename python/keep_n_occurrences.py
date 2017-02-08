import collections


def keep_n_occurrences(seq, n):
    """ Keep up to n occurrences of each value in sequence, return as new list maintaining order """
    val_counts = collections.defaultdict(int)

    def count(i):
        """ Return boolean indicating threshold reached """
        val_counts[i] += 1
        return val_counts[i] <= n

    return [i for i in filter(count, seq)]


if __name__ == "__main__":
    assert keep_n_occurrences([20, 37, 20, 21], 1) == [20, 37, 21]
    assert keep_n_occurrences([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]
