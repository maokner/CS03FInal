def i_cant_believe_it_can_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

#bubble sort
def bubble_sort(iterable):
    def float_largest_to_top(iterable, size):
        swapped = False
        for i in range(size - 1):
            if iterable[i] > iterable[i + 1]:
                iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]
                swapped = True
        return swapped

    size = len(iterable)
    while float_largest_to_top(iterable, size):
        size -= 1

#insertion sort
def insertion_sort(iterable, gap=1):
    for unsorted_index in range(gap, len(iterable)):
        unsorted_data = iterable[unsorted_index]
        k = unsorted_index
        while k >= gap and iterable[k - gap] > unsorted_data:
            iterable[k] = iterable[k - gap]
            k -= gap
        iterable[k] = unsorted_data
#shell sort
def shell_sort(iterable):
    n = len(iterable)
    gap = 1
    while gap < n // 2:
        gap = 2 * gap + 1

    while gap >= 1:
        for i in range(gap, n):
            temp = iterable[i]
            j = i
            while j >= gap and iterable[j - gap] > temp:
                iterable[j] = iterable[j - gap]
                j -= gap
            iterable[j] = temp
        gap = gap // 2





