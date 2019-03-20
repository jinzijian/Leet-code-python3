class Solution(object):
    def restoreIpAddresses(self, s):
        """
       :type s: str
       :rtype: List[str]
       """
        def dfs(s, segment, res, ip):
            if segment == 4:
                if s == '':
                    res.append(ip[1:])
                return
            for i in range(1,4):               
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:],segment+1,res,ip+'.'+s[:i])
                        if s[0] == '0':
                            break                                               
        res = []
        dfs(s, 0, res, '')#segment 初始化为0
        return res
