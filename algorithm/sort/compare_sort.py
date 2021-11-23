from random import randint
from datetime import datetime
from copy import deepcopy
from sort import *

def generate_int(n):
    nums = []
    for i in range(n):
        nums.append(randint(1, 1000000))
    
    return nums

def main():
    size = 1000000
    nums = generate_int(size)

    # python default sort
    start_time = datetime.now()
    nums3 = deepcopy(nums)
    nums3.sort()
    sec_cost = (datetime.now() - start_time).seconds
    print(f"python sort cost {sec_cost} seconds for {size} integer")

    # # selection sort
    # start_time = datetime.now()
    # nums_selection_sort = selection_sort(deepcopy(nums))
    # sec_cost = (datetime.now() - start_time).seconds
    # print(f"selection sort cost {sec_cost} seconds for {size} integer")

    # # insert sort
    # start_time = datetime.now()
    # nums_insert_sort = insert_sort(deepcopy(nums))
    # sec_cost = (datetime.now() - start_time).seconds
    # print(f"insert sort cost {sec_cost} seconds for {size} integer")

    # assert nums3 == nums_insert_sort, "wrong insert sort results"
    # assert nums3 == nums_selection_sort, "wrong selection sort results"

    # # shell sort
    # start_time = datetime.now()
    # nums_shell_sort = shell_sort(deepcopy(nums))
    # sec_cost = (datetime.now() - start_time).seconds
    # print(f"shell sort cost {sec_cost} seconds for {size} integer")

    # assert nums3 == nums_shell_sort, "wrong shell sort results"

    # merge sort
    start_time = datetime.now()
    nums_merge_sort = merge_sort(deepcopy(nums))
    sec_cost = (datetime.now() - start_time).seconds
    print(f"merge sort cost {sec_cost} seconds for {size} integer")

    assert nums3 == nums_merge_sort, "wrong merge sort results"

    # quick sort
    start_time = datetime.now()
    nums_quick_sort = quick_sort(deepcopy(nums))
    sec_cost = (datetime.now() - start_time).seconds
    print(f"quick sort cost {sec_cost} seconds for {size} integer")

    assert nums3 == nums_quick_sort, "wrong quick sort results"

if __name__ == "__main__":
    main()
