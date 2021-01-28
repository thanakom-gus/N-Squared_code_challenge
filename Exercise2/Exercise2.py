
import random
from collections import Counter

def pick10():
     lottery_numbers = list(range(1, 51))
     result = random.sample(lottery_numbers, 10)
     result.sort()
     print(result)
     return result

def unittest_duplicate(numbers):
    items = dict(Counter(numbers))
    for i, num in enumerate(items):
        if items[num] > 1:
            print(f'find duplicate {i} in {numbers}')
##            raise Exception("find a duplicate number")
        
def unittest_unsorted(numbers):
    for i, num in enumerate(numbers):
        if i + 1 != len(numbers) and num > numbers[i+1]:
            print(f'find unsorted value {i} in {numbers}')
##            raise Exception("unsorted")

def unittest_all(numbers):
    unittest_duplicate(numbers)
    unittest_unsorted(numbers)

if __name__ == "__main__":
    # testing
    for _ in range(1,6):
        unittest_all(pick10())

    unittest_all([1, 2 , 3 ,4 , 4, 5, 6, 7, 8 ,9])
    unittest_all([1, 2 , 4 ,3 , 4, 5, 6, 7, 8 ,9])

## finished time 00:44:16.09
