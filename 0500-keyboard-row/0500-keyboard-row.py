class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = set("qwertyuiop")
        r2 = set("asdfghjkl")
        r3 = set("zxcvbnm")

        ans = []
        for w in words:
            s = set(w.lower())
            if s <= r1 or s <= r2 or s <= r3:
                ans.append(w)
        return ans

        