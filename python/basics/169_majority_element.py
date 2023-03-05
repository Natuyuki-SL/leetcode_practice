def majorityElement(nums: list) -> int:
        counter = {}
        n = len(nums)/2
        for num in nums:
            if num in counter:
                counter[num] +=1 
            else: 
                counter[num]=1
            if counter[num] > n:
                return num

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))