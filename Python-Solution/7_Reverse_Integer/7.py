class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10 < x < 10:
            return x
            
        # 1.判断是否为负数
        flag = False  
        if x < 0:
            x = -x
            flag = True

        # 2. 转化为字符串翻转
        x = str(x)[::-1]

        # 3. 去掉多余的零
        while x[0] == '0':
            x = x[1:]

        # 4. 转化为整数并判断溢出
        x = int(x)
        if flag:
            x = -x
        if -2147483648 < x < 2147483647:
            return x
        else:
            return 0
                    

solution = Solution()
r = solution.reverse(0)
print(r)
