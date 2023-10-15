class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            if(s[i] not in s_to_t and t[i] not in t_to_s):
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
            elif(s_to_t.get(s[i]) != t[i] or t_to_s.get(t[i]) != s[i]):
                return False
        return True
