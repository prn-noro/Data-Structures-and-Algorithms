//Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.
import java.util.Arrays;

public class CountTriplets {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int myArr[]= {1, 5, 3, 2};
		int count=0;
		Arrays.sort(myArr);
		
		for(int i=myArr.length-1;i>=0;i--) {
			int myElement=myArr[i];
			int left=0;
			int right=i-1;
			
			while (left<right) {
				if(myArr[left]+myArr[right]==myElement) {
					System.out.println(myArr[left]+" "+myArr[right]+" "+myElement);
					left+=1;
					right-=1;
					count+=1;
				}
				
				else if(myArr[left]+myArr[right]>myElement) {
					right-=1;
				}
				else {
					left+=1;
				}
			}
					
		}
		
	}

}
