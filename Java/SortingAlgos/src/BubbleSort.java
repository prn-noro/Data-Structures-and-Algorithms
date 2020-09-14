
public class BubbleSort {
	
	static void bubbleSort(int myArr[]) {
		int n=myArr.length;
		for(int i=0;i<n-1;i++) {
			for(int j=0;j<n-i-1;j++) {
				if(myArr[j]>myArr[j+1]) {
					int temp=myArr[j];
					myArr[j]=myArr[j+1];
					myArr[j+1]=temp;
				}
			}
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int myArr[]= {5,2,3,4,6,7,1};
		bubbleSort(myArr);
		for(int i:myArr) {
			System.out.println(i);
		}
	}

}
