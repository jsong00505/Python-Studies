# define the method for the print of the result
def printFibonacci(numb):
    # init variables
    firstZero = 0
    firstOne = 0
    secondZero = 0
    secondOne = 0
    resultZero = 0
    resultOne = 0

    # just change recursion method to 'for' statement
    for n in range(numb+1):
        if n == 0:
            firstZero = 1
            firstOne = 0
            resultZero = firstZero
            resultOne = firstOne
        elif n == 1:
            secondZero = 0
            secondOne = 1
            resultZero = secondZero
            resultOne = secondOne
        else:
            resultZero = secondZero + firstZero
            resultOne = secondOne + firstOne
            firstZero = secondZero
            firstOne = secondOne
            secondZero = resultZero
            secondOne = resultOne
    # print
    print str(resultZero) + " " + str(resultOne)


# get number of test cases
numb = int(raw_input().strip())

# get queries from the cases
for n in range(numb):
    q = int(raw_input().strip())
    # do print
    printFibonacci(q)

