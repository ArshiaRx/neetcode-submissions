class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> ConsecutiveNum = new HashSet<>();
        
        for (int i = 0; i < nums.length; i++){
            ConsecutiveNum.add(nums[i]);
        }

        int count = 0;
        
        // Process each element in the array
        for (int num: nums){
            int currentStreak = 1;

            // Check for the start of a sequence
            if (!ConsecutiveNum.contains(num - 1)) {
                int currentNum = num;

                // Continue checking consecutive numbers within the same loop
                while (ConsecutiveNum.contains(currentNum + 1)){
                    currentNum++;
                    currentStreak++;
                }

                // Update the maximum length found
                count = Math.max(count, currentStreak);
            }
        }
        return count;
    }
}