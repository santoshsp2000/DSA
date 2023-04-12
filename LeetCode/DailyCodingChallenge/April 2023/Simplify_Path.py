# 71. Simplify Path
# Leetcode Medium
# Date: 12 April 2023
# TC: O(N)
# SC: O(N)


class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = []
        n = len(path)
        i = 0
        files = 0

        while i < n:
            if path[i] == '/':
                i += 1
            else:
                file = ''
                l = 0
                count = 0

                while i < n and path[i] != '/':
                    file += path[i]
                    if path[i] == '.':
                        count += 1
                    i += 1
                    l += 1

                if l == count:
                    if count == 2 and arr:
                        arr.pop()
                        files -= 1
                    if count > 2:
                        arr.append('.' * count)
                        files += 1
                else:
                    arr.append(file)
                    files += 1

        ans = ''
        if files == 0:
            ans += '/'

        for file in arr:
            ans += '/' + file

        return ans