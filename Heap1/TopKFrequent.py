class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        hashmap = {} # creating the hashmap
        result = [] # creating the resultant array

        bucket = [None for i in range(len(nums)+1)] # creating bucket array with values of None for length of nums 

        for num in nums: # run until num in hashmap the increment the freq by 1
            if num in hashmap:
                hashmap[num] +=1

            else:
                hashmap[num] = 1 # else set the initial freq to 1

        for key,val in hashmap.items(): # for key and value in hashmap if not bucket then create an empty array else append the key value in bucket
            if not bucket[val]:
                bucket[val]=[]
            bucket[val].append(key)

        for i in range(len(bucket)-1,-1,-1): # run until the bucket is not null then add the bucket value to result then subtract the bucket value from k 
            if bucket[i]:
                result += bucket[i]
                k-=len(bucket[i])

            if k == 0: # if k is equal to 0 then break
                break
        return result # returning the result


        