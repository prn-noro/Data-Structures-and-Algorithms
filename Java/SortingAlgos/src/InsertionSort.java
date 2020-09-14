
public class InsertionSort {

	static void insertionSort(int myArr[]) {
		int n=myArr.length;
		
		for(int i=1;i<n;i++) {
			int element=myArr[i];
			int hole=i-1;
			while(hole>=0 && element<myArr[hole]) {
				myArr[hole+1]=myArr[hole];
				hole-=1;
			}
			myArr[hole+1]=element;
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int myArr[]= {5,2,3,4,6,7,1};
		insertionSort(myArr);
		for(int i:myArr) {
			System.out.println(i);
		}
	}

}
