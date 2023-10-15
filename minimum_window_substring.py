class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = collections.defaultdict(int)
        for c in t:
            t_map[c] += 1
        print(t_map)
        m, n = len(s), len(t)
        need = len(t_map)
        have = 0
        l, r = 0, 0
        mS = ""
        ma = float('inf')
        s_map = collections.defaultdict(int)
        for r in range(m):
            s_map[s[r]] += 1
            if t_map.get(s[r], -1) == s_map[s[r]]:
                have += 1
            while have == need and l <= r:
                if r - l + 1 < ma:
                    ma = r - l + 1
                    mS = s[l : r + 1]
                if s_map[s[l]] == t_map.get(s[l], -1):
                    have -= 1
                s_map[s[l]] -= 1
                l += 1
        return mS
