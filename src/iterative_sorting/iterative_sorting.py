# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    if arr is None or len(arr) == 0:
        return []
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"

    counts = []
    sorted_nums = []
    for i in range(0, max(arr) + 1):
        counts.append(0)
        sorted_nums.append(0)

    for i in arr:
        counts[i] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for i in range(len(arr)):
        sorted_nums[counts[arr[i]]-1] = arr[i]
        counts[arr[i]] -= 1

    for i in range(len(arr)):
        arr[i] = sorted_nums[i]

    return arr