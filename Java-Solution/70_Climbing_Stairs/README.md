# 70 - 爬楼梯


## recursive

**思路：** 爬上(n)阶楼梯的方案 = 爬上( n - 1 )阶楼梯的方案 + 爬上( n - 2 )阶楼梯的方案。 如下图：

>实测Java和python都会TLE，都是n=45的时候。

```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2){
            return n;
        }
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
}
```


## DP

**用动态规划实现，这本质上是一个斐波那契数列啊！！**


```java
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        
        int prev2 = 1, prev1 = 2;
        for (int i = 2; i < n; i++){
            int temp = prev2;
            prev2 = prev1;
            prev1 = prev1 + temp;
        }
        return prev1;
    }
}
```