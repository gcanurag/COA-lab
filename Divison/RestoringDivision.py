# a='1101'
# b='1000'

# result=''
# carryIn=0


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


def NOTGATE(a):
    if a == 0:
        return 1
    else:
        return 0


def full_adder(a, b, carryIn):
    sum = XORGATE(XORGATE(a, b), carryIn)

    carryOut = ORGATE(ANDGATE(a, b), ANDGATE(carryIn, XORGATE(a, b)))

    return sum, carryOut


# function to add two numbers
def addTwoNumbers(a, b):
    maximum_length = max(len(a), len(b))

    a = a.zfill(maximum_length)
    b = b.zfill(maximum_length)

    # a,b=a[::-1],b[::-1]

    result = ""
    carry = 0

    for i in range(maximum_length - 1, -1, -1):
        bit1 = int(a[i])
        bit2 = int(b[i])
        sumOfBit, carry = full_adder(bit1, bit2, carry)

        result = str(sumOfBit) + result

        

    return result


# calculating the two's complement of b
def twosComplement(number):
    length=len(number)

    
    y='1'.zfill(length)
    onesComplement=''
    
    for i in range(length - 1, -1, -1):
        onesComplement = str(NOTGATE(int(number[i]))) + onesComplement
        
    twosComplement=addTwoNumbers(onesComplement,y)
    return twosComplement


def subtractor(a, b):
    twos_comp_b = twosComplement(b)
    # print(twos_comp_b)
    result = addTwoNumbers(a, twos_comp_b)
    return result


def divide(q,m):   #q=divident amd m=divisor

    n=len(q)     
    a = "0" * (n + 1)  # if q=1111 then initializw a as 00000
    m = m.zfill(n + 1)
    # print(m)

    for i in range(n):
        a = a[1:] + str(int(q[0]))
        q = q[1:]
        a_minus_m = subtractor(
            a, m
        )  # calculating a-m  but a is a because a is not updated yet
        # print(a_minus_m)
        if (
            int(a_minus_m[0]) == 1
        ):  # a-m is negative and  restore operation is done or a is not updated

            q = q + "0"
            print(a)
            print(q)

        else:
            a = a_minus_m
            q = q + "1"
            print(a)
            print(q)

    print(f"remainder is {a} and quotient is {q}")

def main():
    a = "1110"      #a=divident or q 
    b = "11"

    divide(a,b)

    # print(f"remainder={remainder} quotinet={quotinet}")


if __name__ == "__main__":
    main()
