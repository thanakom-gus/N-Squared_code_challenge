
import math

Roman_digits = {1000:'M',
                900:'CM',
                500:'D',
                400:'CD',
                100:'C',
                50:'L',
                40:'XL',
                10:'X',
                9:'IX',
                5:'V',
                4:'IV',
                1:'I'}


def num_to_ro(num):
    Roman = ''
    for value in Roman_digits:
        if num >= value:
            count = math.trunc(num / value)
            for _ in range(count):
                Roman = Roman + Roman_digits[value]
                num = num - value
    return Roman

if __name__ == "__main__":
    # testing
    test_set = [7,13,38,79,465,1375,4566]
    for i in test_set:
        result = num_to_ro(i)
        print(i, result)


## finished time 00:36:45.68

