from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:

        return sorted(s) == sorted(t)

if __name__ == "__main__":
    print(sorted("caat"))