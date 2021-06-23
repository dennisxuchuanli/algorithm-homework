#题目：加一 https://leetcode-cn.com/problems/plus-one/
#题解1：
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #思路：逆序遍历，加一，如有进位则继续
        #细节：处理越界问题：如首位有进位则插入进位
        jinwei = 1
        for i in range(len(digits)-1,-1,-1):
            total = digits[i] + jinwei
            digits[i] = total%10
            jinwei = int(total/10)
            if jinwei == 0:
                break
        if jinwei != 0:
            digits.insert(0,jinwei)
        return digits
#题解2:
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #思路：先变成整数，加一后，再转换为list
        list2str = ''.join(str(elem) for elem in digits)
        temp = str(int(list2str) + 1)
        result = []
        for elem in temp:
            result.append(int(elem))
        return result