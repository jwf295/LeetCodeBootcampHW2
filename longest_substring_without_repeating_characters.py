class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_length = 0
        max_length = 0
        start_index = 0
        i = 0
        hashmap = {}
        while i < len(s):
            if (s[i] not in hashmap):
                hashmap[s[i]] = 1
                curr_length += 1
                if curr_length > max_length:
                    max_length = curr_length
                i += 1
            else:
                curr_length = 0
                start_index += 1
                i = start_index
                hashmap.clear()
        return max_length
