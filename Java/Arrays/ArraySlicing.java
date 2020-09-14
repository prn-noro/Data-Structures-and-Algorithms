import java.util.Arrays;

public class ArraySlicing {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int myArr[]= {9,8,7,6,5,4,3,2,1};
		int myNew[]=myArr;
		Arrays.sort(myArr);
		
//		The above line sorts both myArr AS WELL AS myNew
		
//		Rather use 
//		int newnewArr[]=myArr.clone();
//		Arrays.sort(myArr);
		
		
//		Index Slicing
		int newArr[]=Arrays.copyOfRange(myArr,2,5);
		
		for(int i:newArr) {
			System.out.println(i);
		}
	}

}
