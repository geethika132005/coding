class Solution:
    def lexicalOrder(self, n: int):

        result = []

        def dfs(curr):

            if curr > n:
                return

            result.append(curr)

            for digit in range(10):

                next_num = curr * 10 + digit

                if next_num > n:
                    break

                dfs(next_num)

        for i in range(1, 10):

            dfs(i)

        return result