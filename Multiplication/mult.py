def ANDGATE(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return 1


def ORGATE(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0


def XORGATE(a, b):
    if a == b:
        return 0
    else:
        return 1


def full_adder(a, b, carryIn):
    sum = XORGATE(XORGATE(a, b), carryIn)

    carryOut = ORGATE(ANDGATE(a, b), ANDGATE(carryIn, XORGATE(a, b)))

    return sum, carryOut


# function to add two numbers
def addTwoNumbers(a, b):
    maximum_length = max(len(a), len(b))

    a = a.zfill(maximum_length)
    b = b.zfill(maximum_length)

    result = ""
    carry = 0

    for i in range(maximum_length - 1, -1, -1):
        bit1 = int(a[i])
        bit2 = int(b[i])
        sumOfBit, carry = full_adder(bit1, bit2, carry)

        result = str(sumOfBit) + result

    if carry:
        result = "1" + result
    

    return result


def multiplier(m, q):  # m = multiplier and q= multiplicand
    length_of_result = len(m) + len(q)
    partial_sum = "0"  # partial sum initialized to 0
    partial_sum = partial_sum.zfill(length_of_result + 1)

    for i in range(len(q)):
        if int(q[i])==1:
            partial_sum=addTwoNumbers(partial_sum, m)

        partial_sum = partial_sum[1:] + '0'

    
    return partial_sum[:-1]


def main():
    a = "101"
    b = "11"

   
    result=multiplier(a,b)
    print(f"{a}*{b}={result}")


if __name__ == "__main__":
    main()
