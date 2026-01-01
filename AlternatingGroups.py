def numberOfAlternatingGroups(self, colors: list[int]) -> int:
    if len(colors) < 3:
        return 0

    ans = 0
    for i in range(0, len(colors)):
        if i == 0:
            if colors[i] != colors[len(colors) - 1] and colors[i] != colors[i + 1]:
                ans += 1
        elif i == len(colors) - 1:
            if colors[i] != colors[0] and colors[i] != colors[i - 1]:
                ans += 1
        elif colors[i] != colors[i - 1] and colors[i] != colors[i + 1]:
            ans += 1

    return ans