class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        def dfs(num,string,res):#注意要定义在里面
            if num == length:
                res.append(string)
                return#???
            for letter in dict[digits[num]]:
                dfs(num+1,string+letter,res)
        dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        length = len(digits)
        if length == 0:
            return []
        res = []
        dfs(0,'',res)
        return res
        
