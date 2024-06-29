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


def addTwoNumbers(a, b):
    maximum_length = max(len(a), len(b))

    a = a.zfill(maximum_length)  # Zero-fill a to match maximum_length
    b = b.zfill(maximum_length)  # Zero-fill b to match maximum_length

    result = ""
    carry = 0
    for i in range(maximum_length - 1, -1, -1):
        bit1 = int(a[i])
        bit2 = int(b[i])
        sumOfBit, carry = full_adder(bit1, bit2, carry)
        result = str(sumOfBit) + result

    return result


def twosComplement(number):
    length = len(number)
    onesComplement = ""
    for i in range(length - 1, -1, -1):
        onesComplement = str(NOTGATE(int(number[i]))) + onesComplement

    twosComplement = addTwoNumbers(
        onesComplement, "1".zfill(length)
    )  # Calculate two's complement with sign extension
    return twosComplement


def subtractor(a, b):
    max_length = max(len(a), len(b))
    a = a.zfill(max_length)  # Zero-fill a to match max_length
    b = b.zfill(max_length)  # Zero-fill b to match max_length
    twos_comp_b = twosComplement(b)
    result = addTwoNumbers(a, twos_comp_b)
    if len(result) > max_length:
        result = result[
            -max_length:
        ]  # Ensure result length matches max_length in case of overflow
    return result


def main():
    a = "10011"
    b = "10010"
    result = subtractor(a, b)
    print(f"{a} - {b} is {result}")


if __name__ == "__main__":
    main()
