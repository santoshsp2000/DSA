// 881. Boats to Save People
// Leetcode Medium
// Date: 3 April 2023
// TC: O(nlog(n))
// SC: O(1)
// Two Pointer Approach


class Solution {

    public int numRescueBoats(int[] people, int limit) {
        int start = 0;
        int end = people.length - 1;
        int ans = 0;
        Arrays.sort(people);

        while (start <= end)
        {
            if (people[start] + people[end] <= limit)
                start += 1;
            end -= 1;
            ans += 1;
        }

        return ans;
    }
}