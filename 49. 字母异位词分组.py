'''看了很久才完全理解 作者大才
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        temp = []
        dict1 = {}
        result = []
        for i in range(len(strs)):
            x = list(strs[i])
            x.sort()
            temp.append("".join(x))
        for i in range(len(temp)):
            if temp[i] not in dict1:dict1[temp[i]] = [i]
            else:dict1[temp[i]].append(i)
        print(dict1)
        for v in dict1:
            for j in range(len(dict1[v])):
                dict1[v][j] = strs[dict1[v][j]]
            result.append(dict1[v])
        return result
