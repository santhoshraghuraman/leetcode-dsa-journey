class Solution:
    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)

        while left <= right:

            speed = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed

            if hours <= h:
                right = speed - 1
            else: 
                left = speed + 1

        return left