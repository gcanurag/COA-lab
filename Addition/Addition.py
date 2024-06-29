# a='1101'
# b='1000'

# result=''
# carryIn=0


def ANDGATE(a,b):
    if a==0 or b==0:
        return 0
    else:
        return 1

def ORGATE(a,b):
    if a==1 or b==1:
        return 1
    else:
        return 0

def XORGATE(a,b):
    if a==b:
        return 0
    else:
        return 1


def full_adder(a,b,carryIn):
    sum = XORGATE(XORGATE(a, b), carryIn)

    carryOut = ORGATE(ANDGATE(a, b), ANDGATE(carryIn, XORGATE(a, b)))

    return sum, carryOut


# function to add two numbers
def addTwoNumbers(a,b):
    maximum_length=max(len(a),len(b))

    a=a.zfill(maximum_length)
    b = b.zfill(maximum_length)

    # a,b=a[::-1],b[::-1]

    result=''
    carry=0

    for i in range(maximum_length - 1, -1, -1):
        bit1=int(a[i])
        bit2=int(b[i])
        sumOfBit,carry=full_adder(bit1,bit2,carry)


        result=str(sumOfBit)+result

        print(result)

        print (carry)

    if carry:
        result='1'+result

    return result


a='1111'
b='1111'

result=addTwoNumbers(a,b)
print(f"The sum of {a} and {b} is {result}")
