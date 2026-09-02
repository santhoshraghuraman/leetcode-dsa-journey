class Solution:
    def lengthOfLongestSubstring(self, s):

        window = set()
        left = 0
        maximum = 0

        for right in range(len(s)):

            while s[right] in window:
                window.remove(s[left])
                left = left + 1

            window.add(s[right])

            maximum = max(maximum, right - left + 1)

        return maximum