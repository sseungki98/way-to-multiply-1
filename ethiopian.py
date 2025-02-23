def get_input():
    num_1 = int(input("Enter the first number > "))
    num_2 = int(input("Enter the second number > "))
    return num_1, num_2

def divide_by_2(number):
    mocks = []
    while number != 0:
        mocks.append(number)
        number = number // 2

    return mocks

def multiple_2(number,len):
    multiple = []
    for _ in range(len):
        multiple.append(number)
        number *= 2

    return multiple

def define_mocks(mocks):
    index = []
    for i in mocks:
        if i%2==1:
            index.append(mocks.index(i))

    return index

def get_answer(index, multiple):
    sum = 0
    for i in index:
        sum += multiple[i]

    return sum

if __name__=='__main__':
    (num_1, num_2) = get_input()
    mocks = []
    multiple = []
    if num_1 > num_2:
        mocks = divide_by_2(num_2)
        multiple = multiple_2(num_1,len(mocks))
    else:
        mocks = divide_by_2(num_1)
        multiple = multiple_2(num_2,len(mocks))
    
    index = define_mocks(mocks)
    sum = get_answer(index, multiple)

    print(f"Result of {num_1} x {num_2} is {sum}.")
