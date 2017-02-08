if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

    # convert list to tuple
    integer_tuple = tuple(integer_list)

    # print the tuple
    print hash(integer_tuple)
