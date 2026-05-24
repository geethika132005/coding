from collections import Counter

class Solution:
    def getHint(self, secret, guess):

        bulls = 0

        secret_left = []
        guess_left = []

        for s, g in zip(secret, guess):

            if s == g:
                bulls += 1

            else:
                secret_left.append(s)
                guess_left.append(g)

        count_secret = Counter(secret_left)

        cows = 0

        for ch in guess_left:

            if count_secret[ch] > 0:

                cows += 1
                count_secret[ch] -= 1

        return str(bulls) + "A" + str(cows) + "B"