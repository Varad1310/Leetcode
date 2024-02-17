class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> a=new HashSet<>();
        for(int i:nums){
            a.add(i);
        }
        int max=0;
        for(int i:nums){
            int x=i-1;
            int curr=0;
            if(!a.contains(x)){
                while(a.contains(x+1)){
                    curr+=1;
                    x+=1;
                }
                max=Math.max(max,curr);
            }
        }
        return max;
    }
}