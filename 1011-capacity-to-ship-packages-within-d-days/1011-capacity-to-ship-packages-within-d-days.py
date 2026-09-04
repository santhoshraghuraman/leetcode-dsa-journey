class Solution:
    def shipWithinDays(self, weights, days):

        left = max(weights)
        right = sum(weights)

        while left <= right:

            capacity = (left + right) // 2

            day_needed = 1
            current_weight = 0

            for weight in weights:

                if current_weight + weight > capacity:
                    day_needed += 1
                    current_weight = 0

                current_weight += weight

            if day_needed <= days:
                right = capacity - 1
            else:
                left = capacity + 1

        return left