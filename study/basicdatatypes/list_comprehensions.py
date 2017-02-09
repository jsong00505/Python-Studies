if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    # my solution
    result = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    result.append([i, j, k])
    print result

    """
    others' solution
    need to be familiar below style...
    """

    # solution 1
    res = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
    print(res)

    # solution 2
    combinations = [[i, j, k] for i in xrange(x + 1) for j in xrange(y + 1) for k in xrange(z + 1)]
    print filter(lambda (i, j, k): i + j + k != n, combinations)