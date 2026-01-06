# bxaaaaxc
#O(N^2)
class Solution:
    #abccxx
    def longestPalindrome(self, s: str) -> str:
        ans = [0,0]
        mem: set[tuple[int, int]] = set()
        for i in range(len(s)):
            mem.add((i, i))

        for i in range(2, len(s) + 1):
            #bbb
            #2, 3 - 3 1
            for j in range(0, len(s) - i + 1):
                is_palin = False
                start = j
                end = j + i - 1
                if i == 2:
                    if s[start] == s[end]:
                        mem.add((start, end))
                        is_palin = True
                else:
                    if s[start] == s[end]:
                        if (start + 1, end - 1) in mem:
                            is_palin = True
                            mem.add((start, end))
                if is_palin:
                    if ans[1] - ans[0] < end - start:
                        ans = [start , end]

        return s[ans[0]: ans[1] + 1]

solution = Solution()
print(solution.longestPalindrome("bbb"))
print(solution.longestPalindrome("babad"))
print(solution.longestPalindrome("cbbd"))
