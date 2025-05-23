import numpy as np
import math

input_list = [18, 10, 20, 19, 17, 9, 8, 73, 62, 25, 14, 33, 42, 11]

def construct_max_heap(input_list, ind):
    if ind < 0 or 2*ind+2 > len(input_list):
        return input_list
    parent = input_list[ind]
    left = input_list[2*ind + 1]
    right = input_list[2*ind + 2] if 2*ind + 2 < len(input_list) else None

    if right == None or left > right:
        if left > parent:
            input_list[ind], input_list[2*ind + 1] = left, parent
            if ind%2 == 2:
                input_list = construct_max_heap(input_list, (ind-2)//2)
            else:
                input_list = construct_max_heap(input_list, (ind-1)//2)

        input_list = construct_max_heap(input_list, ind+1)
    else:
         if right > parent:
            input_list[ind], input_list[2*ind + 2] = right, parent
            if ind%2 == 2:
                input_list = construct_max_heap(input_list, (ind-2)//2)
            else:
                input_list = construct_max_heap(input_list, (ind-1)//2)

         input_list = construct_max_heap(input_list, ind+1)
    return input_list

print("Min heap:", construct_max_heap(input_list, 0))

def max_val_in_min_heap(input_list):
    if len(input_list) == 0:
        return None
    n = len(input_list)

    lower_level = int(np.floor(math.log2(n))+1)
    print("Lower level:", lower_level)

    num_nodes = 2**(lower_level - 1)
    print("Num nodes:", num_nodes)

    max_val = input_list[num_nodes-1]
    for i in range(num_nodes-1, n):
        if input_list[i] < max_val:
            max_val = input_list[i]
    return max_val

print("Max val in min heap:", max_val_in_min_heap(input_list))

