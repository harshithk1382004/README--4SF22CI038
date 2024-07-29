def select_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(arr)ay):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]  
    return array


array = [69, 23, 02, 45, 1]
sorted_array = select_sort(array)
print("Sorted array is:", sorted_array)
