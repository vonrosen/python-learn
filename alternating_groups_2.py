class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        double_list:list[int] = []
        for val in colors:
            double_list.append(val)
        for val in colors:
            double_list.append(val)
        ans = 0
        alt_count = 0
        left = 0
        for right in range(1, len(double_list)):
            if right - left + 1 == k:
                if alt_count == k - 2:
                    ans += 1
                left += 1
                if double_list[left - 1] != double_list[left] and double_list[left] != double_list[left + 1]:
                    alt_count -= 1

            if double_list[right - 1] != double_list[right] and double_list[right] != double_list[right + 1]:
                alt_count += 1

            if left > len(colors) - 1:
                break
        return ans

solution = Solution()
print(solution.numberOfAlternatingGroups([0,1,0,1,0], 3))
