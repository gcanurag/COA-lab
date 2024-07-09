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
    length = len(number)

    y = "1".zfill(length)
    onesComplement = ""

    for i in range(length - 1, -1, -1):
        onesComplement = str(NOTGATE(int(number[i]))) + onesComplement

    twosComplement = addTwoNumbers(onesComplement, y)
    return twosComplement


def subtractor(a, b):
    twos_comp_b = twosComplement(b)
    result = addTwoNumbers(a, twos_comp_b)
    return result


# def BoothsAlgorithm(q, m):  # q=divident amd m=divisor

#     print(f"q is{q} and m is {m}")
#     maximumLength=max(len(q),len(m))

#     # n = len(q)
#     a = "0" * (maximumLength)
#     # m = m.zfill(maximumLength)
#     q = q+'0'

#     print(f"q01-1 is{q} and m is {m}")

#     for i in range(len(m)):
#         q_Zero_q_Minus_One=q[-2:]
#         print(f"q_Zero_q_Minus_One={q_Zero_q_Minus_One}")
#         match q_Zero_q_Minus_One:
#             case "00":
#                 # print("00")
#                 q = a[-1:] + q[:-1]  # first shift q and then a
#                 a = (
#                     a[0] + a[:-1]
#                 )  # if a=0110 then a is updated as a=0011 if a=1001 then a is updated as a=1100
#             case "01":
#                 # print("q0q-1=01")

#                 a = addTwoNumbers(a, m)

#                 q = a[-1:] + q[:-1]
#                 a = (
#                     a[0] + a[:-1]
#                 )
#                 print(a)
#                 print(q)

#             case '10':
#                 print('q0q-1=10')
#                 if i==2:
#                     print(f"a before sub is{a}")
#                     print(f"m is {m}")
#                 a=subtractor(a,m)
#                 q = a[-1:] + q[:-1]
#                 a = (
#                     a[0] + a[:-1]
#                 )
#                 if i==2:
#                     print(f"a after sub is{a}")
#                     print(f"q before updating is{q}")
#                 # print(a)
#                 # print(q)

#                 # Alternative and easy to understand
#                 # a_minus_m = subtractor(a, m)

#                 # temp = (
#                 #     a_minus_m[0] + a_minus_m[:-1]
#                 # )  # if a_minus_m=0110 then temp=0011 if a_minus_m=1001 then temp=1100   by storing in temp , it doesn't matter which one you shift first
#                 # # print(temp)
#                 # q=a_minus_m[-1:]+q[:-1]
#                 # a=temp

#             case '11':

#                 q = a[-1:] + q[:-1]
#                 a = (
#                     a[0] + a[:-1]
#                 )

#     result=a+q[:-1]

#     print(f"Result is {result}")


# def main():
#     a = "1"   #a=101=5 and b=11=3
#     b = "1010"

#     BoothsAlgorithm(a, b)

#     # print(f"remainder={remainder} quotinet={quotinet}")


# if __name__ == "__main__":
#     main()
def BoothsAlgorithm(q, m):
    print(f"q is {q} and m is {m}")
    maximumLength = max(len(q), len(m))

    a = "0" * (maximumLength + 1)  # Initialize a with one extra bit for shifting
    q = q + "0"  # Ensure q is one bit longer for shifting

    print(f"q01-1 is {q} and m is {m}")

    for i in range(len(m)):
        q_Zero_q_Minus_One = q[-2:]
        print(f"q_Zero_q_Minus_One = {q_Zero_q_Minus_One}")
        if q_Zero_q_Minus_One == "00":
            print("00")
            q = a[-1] + q[:-1]  # Shift q to the right by appending a's last bit
            a = a[0] + a[:-1]  # Shift a to the right

        elif q_Zero_q_Minus_One == "01":
            print("01")
            a = addTwoNumbers(a, m)
            q = a[-1] + q[:-1]  # Shift q to the right
            a = a[0] + a[:-1]  # Shift a to the right

        elif q_Zero_q_Minus_One == "10":
            print("10")
            a = subtractor(a, m)
            q = a[-1] + q[:-1]  # Shift q to the right
            a = a[0] + a[:-1]  # Shift a to the right

        elif q_Zero_q_Minus_One == "11":
            print("11")
            q = a[-1] + q[:-1]  # Shift q to the right
            a = a[0] + a[:-1]  # Shift a to the right

        print(f"a = {a}")
        print(f"q before updating = {q}")

    result = a + q[:-1]  # Remove the extra bit from q for final result
    print(f"Result is {result}")


def main():
    a = "1"  # Example values
    b = "1010"

    BoothsAlgorithm(a, b)


if __name__ == "__main__":
    main()
