//Given An array, find index such that sum of elements to right and left and equal
//Example Arr=[0,-3,5,-4,-2,3,1,0]
//Answer = 0 or 3 or 7


public class SumLeftRight {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int myArr[] = {2, 3, 4, 1 ,4, 5};
			
		int sumArr=getSum(myArr);
		
		int localSum=0;
		
		for(int i=0;i<myArr.length;i++) {
			localSum+=myArr[i];
			
			if (localSum==sumArr-localSum+myArr[i]) {
				System.out.println(i);
			}
		}
	}

	static int getSum(int myArr[]) {
		int mySum=0;
		for(int i=0;i<myArr.length;i++) {
			mySum+=myArr[i];
		}
		
		return mySum;
	}
	
}
