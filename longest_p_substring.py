# bxaaaaxc
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                if self.is_palin(j, j + i - 1, s):
                    return s[j:j + i]

        return ""

    def is_palin(self, start: int, end: int, s: str) -> bool:
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def longestPalindromex(self, s: str) -> str:
        self.ans = []
        self.mem: dict(tuple[int], tuple[int]) = {}
        self.search(0, len(s) - 1, 0, len(s) - 1, s)
        return s[self.ans[0]:self.ans[1] + 1]

    def search(self, start, end, o_start, o_end, s: str) -> None:
        if start >= end:
            if self.ans == []:
                self.ans = [o_start, o_end]
            elif self.ans[1] - self.ans[0] < o_end - o_start:
                self.ans = [o_start, o_end]
            return

        if (o_start, o_end) in self.mem:
            return self.mem[(o_start, o_end)]

        if s[start] == s[end]:
            self.search(start + 1, end - 1, o_start, o_end, s)
        else:
            self.search(start, end - 1, start, end - 1, s)
            self.search(start + 1, end, start + 1, end, s)

        self.mem[(o_start, o_end)] = s[self.ans[0]:self.ans[1] + 1]


solution = Solution()
print(solution.longestPalindrome("a"))