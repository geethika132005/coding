from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate, words):

        need = Counter(
            ch.lower()
            for ch in licensePlate
            if ch.isalpha()
        )

        answer = None

        for word in words:

            count = Counter(word.lower())

            valid = True

            for ch in need:

                if count[ch] < need[ch]:
                    valid = False
                    break

            if valid:

                if answer is None or len(word) < len(answer):
                    answer = word

        return answer 