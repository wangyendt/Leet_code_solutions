# coding: utf-8


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        neg_nums = [target - ii for ii in nums]
        id1, id2 = self.find_same_element_in_two_list(nums, neg_nums, target)
        return id1, id2

    def find_same_element_in_two_list(self, list1, list2, target):
        dict1 = {}
        cnt1 = 0
        for l1 in list1:
            dict1[l1] = cnt1
            cnt1 += 1
        cnt2 = 0
        for l2 in list2:
            if dict1.get(l2) is not None and dict1.get(l2) != cnt2:
                return cnt2, dict1.get(l2)
            cnt2 += 1
        return None


if __name__ == '__main__':
    a = [-1, -2, -3, -4, -5]
    ts = Solution()
    x, y = ts.twoSum(a, -8)
    print(x, y)
    pass
