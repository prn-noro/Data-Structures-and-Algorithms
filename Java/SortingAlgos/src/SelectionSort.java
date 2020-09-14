
public class SelectionSort {

	public static void selectionSort(int myArr[]) {
		int minIndex,temp;
		for(int i=0;i<myArr.length-1;i++) {
			minIndex=i;
			for(int j=i+1;j<myArr.length;j++) {
				if(myArr[j]<myArr[minIndex]) {
					minIndex=j;
				}
			}
			temp=myArr[i];
			myArr[i]=myArr[minIndex];
			myArr[minIndex]=temp;
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int myArr[]= {5,2,3,4,6,7,1};
		selectionSort(myArr);
		for(int i:myArr) {
			System.out.println(i);
		}
	}

}
