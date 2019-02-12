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
