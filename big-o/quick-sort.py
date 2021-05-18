def partition(start, end, arr): 
    pivot_index = start
    pivot = arr[pivot_index]
    print("start: ", start, " end: ", end)
    while start < end:
        while start < end and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if (start < end and arr[start] > arr[end]):
            arr[start], arr[end] = arr[end], arr[start]
    
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end

    
def quick_sort(start, end, arr):
    if (start < end): 
        print("quick_sort")
        pivot_index = partition(start, end, arr)
        quick_sort(0, pivot_index - 1, arr)
        quick_sort(pivot_index + 1, end, arr)




# arr = [10, 7, 8, 9, 16, 5, 15, 18]
arr = [1,1,1,1,1,1,1,1,1,1]

# 10, 7, 8, 9, 16, 5, 15, 18
# 10, 7, 8, 9, 5, 16, 15, 18
# 10, 7, 8, 9, 5, 16, 15, 18



# 1, 1, 1, 1

quick_sort(0, len(arr) - 1, arr)
print(arr)
