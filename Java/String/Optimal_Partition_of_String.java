// 2405. Optimal Partition of String
// Leetcode Medium
// TC: O(N)
// SC: O(1)


class Solution {
    public int partitionString(String s) {
        int i = 0;
        Map<Character,Boolean> letters = new HashMap<Character,Boolean>();
        int ans = 0;
        while (i < s.length())
        {
            if(letters.containsKey(s.charAt(i)))
            {
                ans += 1;
                letters.clear();
            }
            letters.put(s.charAt(i), true);
            i++;
        }
        return ans+1;
    }
}