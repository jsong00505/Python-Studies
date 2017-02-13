if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

    # arr sorted in disorder
    arr.sort(reverse=True)

    # index 0 in arr is the largest number
    largest = arr[0]

    # iterate arr for searching second largest number
    # if not equal with largest, that is the second largest number because of sorting arr
    for i in arr:
        if i != largest:
            print i
            break


