class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        List<Integer> hs=new ArrayList<>();
        int n=nums.length;
        for(int i=0;i<n;i++){
            Arrays.sort(nums);
            int temp=nums[i];
            if(temp==target){
                hs.add(i);
            }
        }
        return hs;
    }
}