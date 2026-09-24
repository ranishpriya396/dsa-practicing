nums = [22,2,2,3,5,6,8,89,0]
def freq_mapping(nums):
    freq = dict()
    for i in range(0,len(nums)):
        if nums[i] in freq:
           freq[nums[i]] +=1
        else :
           freq[nums[i]] = 1
    return freq
# print(freq_mapping(nums))

def hashing(nums):
    freq = dict()
    for i in range(0,len(nums)):
        freq[nums[i]] = freq.get(nums[i],0)+1
    return freq
print(hashing(nums))
