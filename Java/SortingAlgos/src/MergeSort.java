
public class MergeSort {
	
	static void merge(int myArr[],int start,int mid,int end) {
		int leftSize=mid-start+1;
		int rightSize=end-mid;
		
		int leftArr[]=new int[leftSize];
		int rightArr[]=new int[rightSize];
		
		for(int i=0;i<leftSize;i++) {
			leftArr[i]=myArr[i+start];
		}
		for(int j=0;j<rightSize;j++) {
			rightArr[j]=myArr[j+mid+1];
		}
		
		
		int i=0,j=0;
		int k=start;
		
		while(i<leftSize && j<rightSize) {
			if(leftArr[i]<=rightArr[j]) {
				myArr[k]=leftArr[i];
				i+=1;
				k+=1;	
			}
			else {
				myArr[k]=rightArr[j];
				j+=1;
				k+=1;
			}
		}
		
		while(i<leftSize) {
			myArr[k]=leftArr[i];
			i+=1;
			k+=1;
		}
		
		while(j<rightSize) {
			myArr[k]=rightArr[j];
			j+=1;
			k+=1;
		}
		

	}
	
	static void mergeSort(int myArr[],int start,int end) {
		if(start<end) {
			int mid=(start+end)/2;
			mergeSort(myArr,start,mid);
			mergeSort(myArr,mid+1,end);
			
			
			merge(myArr,start,mid,end);
			
			
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int myArr[]= {10,7,8,9,1,5};
		mergeSort(myArr,0,myArr.length-1);
		for(int i:myArr) {
			System.out.println(i);
		}
	}

}
