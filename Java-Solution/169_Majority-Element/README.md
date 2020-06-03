# 169 - 求众数

## 一、字典（hash)
**时间复杂度: O(n)**
思路：
使用map计算每个元素出现的次数，若出现次数**大于**`⌊ n/2 ⌋`则返回，无需考虑特殊情况。

```Java
class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int n = nums.length;
        int res = -1;

        for (int num:nums) {
            if (!map.containsKey(num)) {
                map.put(num, 1);
            } else {
                map.put(num, map.get(num) + 1);
            }
            if (map.get(num) > n / 2) {
                    return num;
                }
        }
        return res;
    }
}
```

## 二、排序
**时间复杂度: O(n logn)**
思路：  
众数出现的次数大于`⌊ n/2 ⌋`，那么排序后数组的中位数一定是众数。  

```java
class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length / 2];
    }
}
```


## 三、分治法
**时间复杂度: O(n logn)**
```java
class Solution {
    private int countInRange(int[] nums, int num, int l, int r) {
        int cnt = 0;
        for (int i = l; i <= r; i++){
            if (nums[i] == num) {
                cnt++;
            }
        }
        return cnt;
    }

    private int majorityElementInRange(int[] nums, int l, int r) {
        // base case:只剩一个元素，则其为众数
        if (l == r) {
            return nums[l];
        }

        // 分治
        int mid = (r - l) / 2 + l;
        int left = majorityElementInRange(nums, l, mid);
        int right = majorityElementInRange(nums, mid + 1, r);

        // 返回出现次数较多的
        if (left == right) {
            return left;
        }
        int leftCount = countInRange(nums, left, l, mid);
        int rightCount = countInRange(nums, right, mid + 1, r);
        return leftCount > rightCount ? left : right;
    }

    public int majorityElement(int[] nums) {
        return majorityElementInRange(nums, 0, nums.length - 1);
    }
}
```


## 四、位操作
**时间复杂度: O(n)**
思路：  
将众数按位来建立。将每个数看做32位的二进制数，从0到31位，对每个数字统计下该位上0和1的个数，如果这一位1的个数大于一半，说明众数中这一位是1，否则众数的这一位是0.
```java
class Solution {
    public int majorityElement(int[] nums) {
        int major = 0;
        int k = nums.length >> 1;
        for (int i = 0; i < 32; i++) {
            int bitCount = 0;
            for (int num: nums) {
                bitCount += num >> i & 1;
                if (bitCount > k) {
                    major += 1 << i;
                    break;
                }
            }
        }
        return major;
    }
}

```


## 五、投票算法
**时间复杂度: O(n)**
![moore](images/moore.png)
思路：  
1. 两个变量candidate和count。candidate记录当前可能的候选众数，count保存该候选众数出现的次数。
2. 遍历数组nums：
	- 若当前元素与candidate相同，则计数count + 1；
	- 否则若count == 0则说明这个candidate不可能是众数了，将更新candidate为当前元素；
	- 否则count - 1。
3. 因为每一对不一样的数都会消掉，而众数的数量大于一半，所以最终留下的candidate即为“当选的”众数。

```java
class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        Integer candidate = null;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }
}

```