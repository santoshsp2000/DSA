class Solution:

    def generate_pascal_triangle(self, numRows: int):
        ans = []

        for i in range(1, numRows + 1):
            row = [1]
            n = i
            f = 1

            for j in range(1, n):
                f *= (n - j)
                f //= (j)
                row.append(f)

            ans.append(row)

        return ans