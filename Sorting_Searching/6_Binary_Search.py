# prerequest => array should be sorted 
arr = [9,10,12,14,17,19,20]
key = 7
def binary_search(arr,key):
    start = 0
    end = len(arr)-1
    while start <= end :
        mid = (start+end)//2
        if arr[mid] == key :
            return mid 
        elif arr[mid] > start :
            start = mid+1
        else :
            end = mid-1
    return "key not found"
print(binary_search(arr,key))

