def findKthLargest(nums: list, k: int) -> int:
        counter = {}
        zero_count = 0
        for num in nums:
            if num in counter:
                counter[num] += 1 
            else:
                if num == 0:
                    zero_count +=1
                else:
                    counter.update({num:1})
        maximum = max(counter)
        while k > 0:
            if maximum == 0:
                k = k - zero_count
            elif maximum in counter:
                k = k - counter.get(maximum)
            maximum -= 1
        return maximum + 1

print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))
print(findKthLargest([-1,2,0], 2))