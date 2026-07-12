class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l,r = 0, len(nums)-1                    #basically left pointer points to index 0 and right poiner points to last index which is length of array-1

        while l <= r:
            mid = (l+r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:            #since its a sorted array, nd target > mid no. of array,
                l = mid + 1                   # we search in the greater half i.e. to the right portion of mid, hence we update left pointer 
                                                    #so that it points to the index after mid
            else:                                 # if target < nums[mid] , similarly, we shud search smaller half of the array, so update right pointer
                    r = mid-1
            
        return l                      #when we dont find the target in len(nums), we return l to handle edge cases, see yt vid
        
        #Binary Search Algorithm
        #we couldve iterated thru each index and checked against the target value, but then time cmplexity would be O(n), but because we used binary search, our time complexity is much more efficient i.e. O(logn)