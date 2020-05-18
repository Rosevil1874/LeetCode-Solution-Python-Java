# 20 - 有效的括号

使用栈和map：
```java
class Solution {
    private static final Map<Character, Character> map = new  HashMap<Character, Character>() {{
        put('}','{'); put(']','['); put(')','('); 
    }};

    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            // 如果是左括号就入栈
            if (map.containsValue(c)) {
                stack.push(c);
            }
            // 如果是右括号就判断和栈顶是否匹配
            else if(map.containsKey(c)) {
                char top_elem = stack.empty() ? '#' : stack.pop();
                if (top_elem != map.get(c)) {
                    return false;
                }
            }
            
        }
        return stack.empty();
    }
}
```