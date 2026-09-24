nums = [1,11,9,10,3,4,5]
def bubble_sort(nums):
    for i in range(0,len(nums)):
        swapped = False
        for j in range(len(nums)-i-1):
            if nums[j]> nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]
                swapped = True 
    return nums
print(bubble_sort(nums))

