students = {}

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())

    # set inputs in dictionary
    if score not in students.keys():
        students[score] = [name]
    else:
        students[score].append(name)

# init values for getting the result
cnt = 1
position = -1

# sorting keys and get a postion of the second lowest score
for s in sorted(students.iterkeys()):
    if cnt == 2:
        position = s
        break
    cnt = cnt + 1

# print all
for v in sorted(students[position]):
    print v