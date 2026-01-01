def quick_sort(arr: list[int]):
    _quick_sort(0, len(arr) - 1, arr)

    # for i in range(0, len(arr)):
    #     print(arr[i])
    #
    # print(" ")

def _quick_sort(start: int, end: int, arr: list[int]):
    if start >= end:
        return
    pivot = find_pivot(start, end, arr)
    _quick_sort(start, pivot - 1, arr)
    _quick_sort(pivot + 1, end, arr)

## [11,3,2,10,4]
## [3,11,2,10,4]
## [3,2,11,10,4] 2
## [3,2,4,10,11]
def find_pivot(start: int, end: int, arr: list[int]):
    pivot_value = arr[end]
    new_pivot_index = start

    for i in range(start, end):
        if arr[i] < pivot_value:
            tmp = arr[new_pivot_index]
            arr[new_pivot_index] = arr[i]
            arr[i] = tmp
            new_pivot_index += 1

    tmp = arr[new_pivot_index]
    arr[new_pivot_index] = pivot_value
    arr[end] = tmp

    return new_pivot_index

quick_sort([11,10])
quick_sort([11,3,2])
quick_sort([11,3,2,10,4])
quick_sort([11,100,101,2,3,2,10,10,34])
