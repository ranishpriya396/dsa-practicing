nums = [12,33,5,66,3,5,6]
def selection_sort(arr):
    for i in range(0,len(arr)):
        min_i = i 
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_i]:
                min_i = j 
        arr[i],arr[min_i] = arr[min_i], arr[i]
    return arr
print(selection_sort(nums))
