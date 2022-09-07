var searchInsert = function(nums, target) {
    let left = 0, right = nums.length-1, mid, cur;
    while (left <= right){
        mid = Math.floor((right + left)/2);
        if (nums[mid] == target){
            return mid;
        }
        if (target > nums[mid]){
            left = mid +1
            cur = left;
        }
        if (target < nums[mid]) {
            cur = mid
            right = mid - 1;
        }
    }
    return cur
};
