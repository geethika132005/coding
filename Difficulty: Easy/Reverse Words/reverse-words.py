class Solution:
    def reverseWords(self, s):
        words = [word for word in s.split('.') if word]
        return ".".join(words[::-1])