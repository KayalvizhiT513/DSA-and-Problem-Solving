import numpy as np
import math

input_list = [18, 10, 20, 19, 17, 9, 8, 73, 62, 25, 14, 33, 42, 11]

def construct_min_heap(input_list, ind):
    if ind < 0 or 2*ind+2 > len(input_list):
        return input_list
    parent = input_list[ind]
    left = input_list[2*ind + 1]
    right = input_list[2*ind + 2] if 2*ind + 2 < len(input_list) else None

    if right == None or left < right:
        if left < parent:
            input_list[ind], input_list[2*ind + 1] = left, parent
            if ind%2 == 2:
                input_list = construct_min_heap(input_list, (ind-2)//2)
            else:
                input_list = construct_min_heap(input_list, (ind-1)//2)

        input_list = construct_min_heap(input_list, ind+1)
    else:
         if right < parent:
            input_list[ind], input_list[2*ind + 2] = right, parent
            if ind%2 == 2:
                input_list = construct_min_heap(input_list, (ind-2)//2)
            else:
                input_list = construct_min_heap(input_list, (ind-1)//2)

         input_list = construct_min_heap(input_list, ind+1)
    return input_list

def heap_sort(input_list):
    n = len(input_list)
    sorted_list = []
    for _ in range(n):
        input_list = construct_min_heap(input_list, 0)
        sorted_list.append(input_list[0])
        input_list[0] = input_list[-1]
        input_list.pop()

    return sorted_list    

print("Sorted list:", heap_sort(input_list))

