'''python OrderedDict()
如果：| nums[i] - nums[j] | <= t 式a
等价：| nums[i] / t - nums[j] / t | <= 1 式b
推出：| floor(nums[i] / t) - floor(nums[j] / t) | <= 1 式c
等价： floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}式d
其中式b是式c的充分非必要条件，因为逆否命题与原命题等价，所以：
如果： floor(nums[j] / t) ∉ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}非d
推出：| nums[i] - nums[j] | > t 非a
如果 popitem(last=False) 将弹出第一个插入的键值对
'''
from collections import OrderedDict
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k<1 or t<0:
            return False
        _dict=OrderedDict()
        for num in nums:
            key=num if not t else num//t
            for m in (_dict.get(key-1),_dict.get(key),_dict.get(key+1)):
                if m is not None and abs(num-m)<=t:
                    return True
            if len(_dict)==k:
                _dict.popitem(False)
            _dict[key]=num
        return False
