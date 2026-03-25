double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
        int s=nums1Size+nums2Size;
        int nums3[s];
        int i=0;
        int j=0;
        int k=0;
        while(i<nums1Size){
            nums3[i++]=nums1[j++];
        }
        while(i<s){
            nums3[i++]=nums2[k++];
        }
        for(int i=0;i<s;i++){
            for(int j=i+1;j<s;j++){
                if (nums3[i]>nums3[j]){
                    int temp=nums3[i];
                    nums3[i]=nums3[j];
                    nums3[j]=temp;
                }
            }
        }
        if (s%2!=0){
            return nums3[s/2];
        }
        else{
            float y=(nums3[s/2]);
            float z=(nums3[(s/2)-1]);
            return (y+z)/2;
        }
   
}