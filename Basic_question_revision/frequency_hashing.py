# 1. store in frequency :
nums = [5,6,7,7,1,9,111,5,1,1,1]
freq = dict()
for i in range(0,len(nums)) :
    if nums[i] in  freq:
        freq[nums[i]] +=1 
    else : 
        freq[nums[i]] =1
print(freq)
# print(freq.keys())
# print(freq.values())
# print(freq.items())

# 2. hashing :
hash = dict()
for i in range(0,len(nums)):
    hash[nums[i]] = hash.get(nums[i],0)+1
print(hash)