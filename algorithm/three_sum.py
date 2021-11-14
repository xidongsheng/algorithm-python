import os
from datetime import datetime
import random

def count_sum_zero(nums):
    l = len(nums)
    count = 0
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if nums[i] + nums[j] + nums[k] == 0:
                    count += 1

    return count


def count_sum_zero_fast(nums):
    l = len(nums)
    count = 0 

    for i in range(l):
        for j in range(i+1, l):
            left = 0 - nums[i] -nums[j]
            try:
                pos = nums.index(left, j+1, l)
                if pos!=i and pos!=j:
                    count += 1
            except ValueError:
                continue
    
    return count


def main():
    # nums = [5, 3, -4, -1, 1]
    print(os.getcwd())
    nums = []
    file_time = datetime.now()
    f = open('algs4-data/1Mints.txt', 'r')
    try:
        for line in f.readlines():
            nums.append(int(line))
    finally:
        f.close()

    start_time = datetime.now()
    print("reading file cost {}".format(start_time - file_time))
    # change the algorithm to compare the running time
    print(count_sum_zero_fast(nums))
    print(datetime.now() - start_time)


def randam_test(n):
    nums = []
    for i in range(n):
        nums.append(random.randint(-100000, 100000))

    start_time = datetime.now()
    results = count_sum_zero_fast(nums)
    sec_cost = (datetime.now() - start_time).seconds

    print(f"for size {n}, result is {results} cost {sec_cost} seconds", )


if __name__ == "__main__":
    # main()
    randam_test(1000)
    randam_test(2000)
    randam_test(4000)
    randam_test(8000)
# for size 1000, result is 622 cost 2 seconds
# for size 2000, result is 4967 cost 20 seconds
# for size 4000, result is 40130 cost 165 seconds
# for size 8000, result is 316718 cost 1860 seconds