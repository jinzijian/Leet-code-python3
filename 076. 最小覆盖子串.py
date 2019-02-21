class Solution:
    def minWindow(self, s, t):
        """
        1. 窗口范围：[l...r]，初始值-[0..-1]。
        2. 辅助变量：target_counter存放t，cur_dict存放当前符合条件的字符。
        3. 移动条件：当前字符串中是否是目标字符串的父集，不是右边界右移动，是左边界右移。
        4. 改变结果：记录符合条件中最短的字符串。
        5. 辅助函数：判断cur_dict中每个key是否在目标集中，每个value是否都小于等于目标集中对应的value。
        """
        from collections import Counter

        left, right = 0, -1

        target_counter = Counter(t)
        cur_dict = {}

        found_sub_str = None

        while left < len(s):

            if right + 1 < len(s) and not self._is_sub(cur_dict, target_counter):
                cur_dict[s[right + 1]] = cur_dict.setdefault(s[right + 1], 0) + 1
                right += 1
            else:
                cur_dict[s[left]] -= 1
                if cur_dict[s[left]] == 0:
                    del cur_dict[s[left]]

                left += 1

            if self._is_sub(cur_dict, target_counter):
                if found_sub_str is None or right - left + 1 < len(found_sub_str):
                    found_sub_str = s[left:right + 1]

        return found_sub_str if found_sub_str is not None else ''

    def _is_sub(self, parent, child):
        for i, v in child.items():
            if i not in parent:
                return False
            elif child[i] > parent[i]:
                return False
        return True
