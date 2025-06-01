import math

# Max Heap
def construct_max_heap(heap, index):
    while index > 0:
        parent = (index - 1) // 2
        if heap[parent] < heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
            index = parent
        else:
            break
    return heap

# Min Heap
def construct_min_heap(heap, index):
    while index > 0:
        parent = (index - 1) // 2
        if heap[parent] > heap[index]:
            heap[parent], heap[index] = heap[index], heap[parent]
            index = parent
        else:
            break
    return heap

# Extract top (max from max-heap)
def extract_max(heap):
    if not heap:
        return None
    top = heap[0]
    heap[0] = heap.pop()
    index = 0
    size = len(heap)
    while index < size:
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < size and heap[left] > heap[largest]:
            largest = left
        if right < size and heap[right] > heap[largest]:
            largest = right
        if largest == index:
            break
        heap[index], heap[largest] = heap[largest], heap[index]
        index = largest
    return top

# Extract top (min from min-heap)
def extract_min(heap):
    if not heap:
        return None
    top = heap[0]
    heap[0] = heap.pop()
    index = 0
    size = len(heap)
    while index < size:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        if left < size and heap[left] < heap[smallest]:
            smallest = left
        if right < size and heap[right] < heap[smallest]:
            smallest = right
        if smallest == index:
            break
        heap[index], heap[smallest] = heap[smallest], heap[index]
        index = smallest
    return top

# Median logic
def get_median(max_heap, min_heap):
    if len(max_heap) > len(min_heap):
        return max_heap[0]
    elif len(min_heap) > len(max_heap):
        return min_heap[0]
    else:
        return (max_heap[0] + min_heap[0]) / 2

input_list = [18, 10, 20, 19, 17, 9, 8]
max_heap = []
min_heap = []

for num in input_list:
    # Insert to max heap the first half and min heap the second half
    if not max_heap or num <= max_heap[0]:
        max_heap.append(num)
        construct_max_heap(max_heap, len(max_heap) - 1)
    else:
        min_heap.append(num)
        construct_min_heap(min_heap, len(min_heap) - 1)

    # Balance heaps
    if len(max_heap) > len(min_heap) + 1:
        val = extract_max(max_heap)
        min_heap.append(val)
        construct_min_heap(min_heap, len(min_heap) - 1)
    elif len(min_heap) > len(max_heap):
        val = extract_min(min_heap)
        max_heap.append(val)
        construct_max_heap(max_heap, len(max_heap) - 1)

# Output
print("Max Heap (Lower half):", max_heap)
print("Min Heap (Upper half):", min_heap)
print("Median:", get_median(max_heap, min_heap))
