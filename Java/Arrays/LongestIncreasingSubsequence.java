//NOTE : This is for only contiguous Subsequence. REMEMBER THAT

import java.util.Arrays;
import java.util.HashMap;

public class LongestIncreasingSubsequence {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashMap<Integer,Integer> myMap=new HashMap<Integer,Integer>();
		int myArr[]= {3, 10, 2, 1, 20};
		int maxLen=1;
		myMap.put(0,1);
		for(int i=1;i<myArr.length;i++) {
			if(myArr[i]>myArr[i-1]) {
				myMap.put(i,myMap.get(i-1)+1);
				if(myMap.get(i)>maxLen) {
					maxLen=myMap.get(i);
				}
			}
			else{
				myMap.put(i,1);
			}
		}
//		System.out.println(maxLen);
	
		int starIndex=0;
		for(int i:myMap.keySet()) {
			if (maxLen==myMap.get(i)) {
				starIndex=i-maxLen+1;
				break;
			}
		}
		int newArr[]=Arrays.copyOfRange(myArr, starIndex, starIndex+maxLen);
		for(int i:newArr) {
			System.out.println(i);
		}
	}
	


}
