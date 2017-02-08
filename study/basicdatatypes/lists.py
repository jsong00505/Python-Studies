if __name__ == '__main__':
    N = int(raw_input())
    arr = []

    for i in range(N):
        line = raw_input()
        values = line.split(' ')

        if values[0] == "insert":
            arr.insert(int(values[1]), int(values[2]))
        elif values[0] == "print":
            print arr
        elif values[0] == "remove":
            arr.remove(int(values[1]))
        elif values[0] == "append":
            arr.append(int(values[1]))
        elif values[0] == "sort":
            arr.sort()
        elif values[0] == "pop":
            arr.pop()
        elif values[0] == "reverse":
            arr.reverse()
