def removeDuplicates(nums, answer) :
        if len(nums)==1: 
            return 1
        cur = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                #print('skipped', nums[i])
                continue
            else:
                cur+=1
                nums[cur] = nums[i]
                #print('amended position', cur,'with',nums[i])
        ans = cur+1
        if answer == ans:
            return 'correct'

print(removeDuplicates([0, 1, 2, 3], 4))
print(removeDuplicates([0, 0, 1, 1, 2, 2, 3, 4], 5))
print(removeDuplicates([1,1,2], 2))