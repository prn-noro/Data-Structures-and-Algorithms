
public class QuickSort {

	
	static int partition(int myArr[],int start,int end) {
		int pivot=myArr[end];
		int partitionIndex=start;
		
		for(int i=start;i<end;i++) {
			if(myArr[i]<=pivot) {
				int temp=myArr[partitionIndex];
				myArr[partitionIndex]=myArr[i];
				myArr[i]=temp;
				
				partitionIndex+=1;
			}
		}
		
		int temp=myArr[partitionIndex];
		myArr[partitionIndex]=pivot;
		myArr[end]=temp;
		
		return partitionIndex;
	}
	
	static void quickSort(int myArr[],int start,int end) {
		if(start<end) {
			int pi=partition(myArr,start,end);
			quickSort(myArr,start,pi-1);
			quickSort(myArr,pi+1,end);
			
			
		}
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int myArr[]= {10,7,8,9,1,5};
		quickSort(myArr,0,myArr.length-1);
		for(int i:myArr) {
			System.out.println(i);
		}
	}

}
