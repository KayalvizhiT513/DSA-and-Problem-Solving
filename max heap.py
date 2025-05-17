input_list = [18, 10, 20, 19, 17, 9, 8]

def construct_max_heap(input_list, ind):
    if ind < 0 or 2*ind+2 > len(input_list):
        return input_list
    parent = input_list[ind]
    left = input_list[2*ind + 1]
    right = input_list[2*ind + 2]

    if left > right:
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

print(construct_max_heap(input_list, 0))

def construct_min_heap(input_list, ind):
    if ind < 0 or 2*ind+2 > len(input_list):
        return input_list
    parent = input_list[ind]
    left = input_list[2*ind + 1]
    right = input_list[2*ind + 2]

    if left < right:
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

print(construct_min_heap(input_list, 0))
