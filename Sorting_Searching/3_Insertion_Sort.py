arr = [56,44,3,23,11,2,231,0]
def insertion_sort(nums):
    for i in range(0,len(nums)):
        sort_element = arr[i]
        j = i 
        while j > 0 and arr[j-1] > sort_element :
            arr[j] = arr[j-1]
            j = j-1
        arr[j] = sort_element 
    return arr
print(insertion_sort(arr))
