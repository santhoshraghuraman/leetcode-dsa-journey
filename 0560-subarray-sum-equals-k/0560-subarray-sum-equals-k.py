class Solution:
    def subarraySum(self, nums, k):

        count = 0
        prefix_sum = 0
        seen = {0:1}

        for i in nums:
            prefix_sum = prefix_sum + i
            required = prefix_sum - k

            if required in seen:
                count = count + seen[required]

            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return count