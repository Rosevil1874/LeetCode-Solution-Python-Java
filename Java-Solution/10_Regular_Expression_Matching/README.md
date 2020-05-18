# 10 - 正则表达式匹配



## 递归

1. 若正则表达式的长度为0，字符串长度也为0时匹配，否则不匹配；
2. 若正则表达式的长度为1，当字符串长度也为1，且两字符相等或表达式为'.'时匹配，否则不匹配；
3. 由于正则表达式中'\*'只能出现在字符后，所以从第二个字符（下标为1）开始判断。
4. 若正则表达式第二个字符非'\*'，且字符串长度为0，不匹配。若其为'\*'，则第一个字符匹配且后面的剩余部分都匹配（这里使用递归判断子串是否匹配）就匹配。
5. 若正则表达式第二个字符为'\*'，则字符串的第一个字符一定是匹配的。接下来递归判断字符串与表达式第三个字符开始的子串是否匹配，若匹配返回True。否则判断字符串第二个字符开始的子串与表达式是否匹配（一个个字符一次与与'\*'匹配）。


```java
class Solution {
    public boolean isMatch(String s, String p) {
        // corner case
        if (p.isEmpty()) {
            return s.isEmpty();
        }

        // check first character
        boolean first_match = (!s.isEmpty() && (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.'));

        // check second character
        if (p.length() >= 2 && p.charAt(1) == '*') {
            // 1. 匹配0个字符，2.若首字符匹配可匹配一个字符
            return (isMatch(s, p.substring(2)) || (first_match && isMatch(s.substring(1), p)));
        } 
        // 若首字符匹配可匹配一个字符
        else {
            return first_match && (isMatch(s.substring(1), p.substring(1)));
        }
    }
}
```


## 动态规划

This problem has a typical solution using Dynamic Programming. We define the state P[i][j] to be true if s[0..i) matches p[0..j) and false otherwise. Then the state equations are: 
>1. P[i][j] = P[i - 1][j - 1], if p[j - 1] != ‘\*’ && (s[i - 1] == p[j - 1] || p[j - 1] == ‘.’); 
2. P[i][j] = P[i][j - 2], if p[j - 1] == ‘\*’ and the pattern repeats for 0 times; 
3. P[i][j] = P[i - 1][j] && (s[i - 1] == p[j - 2] || p[j - 2] == ‘.’), if p[j - 1] == ‘\*’ and the pattern repeats for at least 1 times. 

Putting these together, we will have the following code.

以下代码关于dp[i][j]的定义与以上分析相反，即dp[i][j]为True表示p[0..i) matches s[0..j)。比楼上递归快多了。

```java
class Solution {
    public boolean isMatch(String s, String p) {
        if(s==null||p==null)
            return false;
       int rows = s.length();
       int columns = p.length();
       boolean[][]dp = new boolean[rows+1][columns+1];
       //s和p两个都为空，肯定是可以匹配的，同时这里取true的原因是
       //当s=a，p=a，那么dp[1][1] = dp[0][0]。因此dp[0][0]必须为true。
       dp[0][0] = true;
        for(int j=1;j<=columns;j++)
        {   
            //p[j-1]为*可以把j-2和j-1处的字符删去，只有[0,j-3]都为true才可以
            //因此dp[j-2]也要为true，才可以说明前j个为true
            if(p.charAt(j-1)=='*'&&dp[0][j-2])
                dp[0][j] = true;
        }

        for(int i=1;i<=rows;i++)
        {
            for(int j=1;j<=columns;j++)
            {
                char nows = s.charAt(i-1);
                char nowp = p.charAt(j-1);
                if(nows==nowp)
                {
                    dp[i][j] = dp[i-1][j-1];
                }else{
                    if(nowp=='.')
                        dp[i][j] = dp[i-1][j-1];
                    else if(nowp=='*')
                    {
                        //p需要能前移1个。（当前p指向的是j-1，前移1位就是j-2，因此为j>=2）
                        if(j>=2){
                            char nowpLast = p.charAt(j-2);
                            //只有p[j-2]==s[i-1]或p[j-2]==‘.’才可以让*取1个或者多个字符：
                            if(nowpLast==nows||nowpLast=='.')
                                dp[i][j] = dp[i-1][j]||dp[i][j-1];
                            //不论p[j-2]是否等于s[i-1]都可以删除掉j-1和j-2处字符：
                            dp[i][j] = dp[i][j]||dp[i][j-2];
                        }
                    }
                    else
                        dp[i][j] = false;
                }
            }
        }
        return dp[rows][columns];
    }
}

```