class Solution {
    public static int search(int[] nums, int target) {
        int tempIndex = 0;
        int startIndex = 0 ;
        int endIndex = nums.length;
        while(nums[tempIndex] != target){
            tempIndex = (endIndex+startIndex)/2;
            if(nums[tempIndex] > target){
                endIndex = tempIndex;
            }else if(nums[tempIndex]<target){
                startIndex = tempIndex;
            }else{break;}

        }
        return tempIndex;
    }
    public static void main(String[] args){
        int[] test1 = {-1,0,3,5,9,12};
        System.out.println(search(test1, 9));
    }

    
}