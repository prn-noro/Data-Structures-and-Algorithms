//# You are given an array. You have to find whether there is a triplet of index i, j, k such that i<j<k and a[i]<a[j]<a[k].
//# Expected time complexity O(n).

public class TripletSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int myArr[] = {12, 3, 10, 5, 6, 2, 30} ;
		int len=myArr.length;
		int small[]= new int[len];
		small[0]=-1;
		int minElem=myArr[0];
		int minIndex = 0;
		for(int i=1;i<myArr.length;i++) {
			if(myArr[i]<minElem) {
				minElem=myArr[i];
				minIndex=i;
				small[i]=-1;
			}
			else {
				small[i]=minIndex;
			}
		}
		int big[] =new int[len];
		big[len-1]=-1;
		int maxElem=myArr[len-1];
		int maxIndex=len-1;
		for(int i=len-2;i>-1;i--) {
			if(myArr[i]>maxElem) {
				maxElem=myArr[i];
				maxIndex=i;
				big[i]=-1;
			}
			else {
				big[i]=maxIndex;
			}
		}
		for(int i=0;i<myArr.length;i++) {
			if(myArr[i]!=-1 && small[i] !=-1 && big[i]!=-1) {
				System.out.println("The three elements are "+myArr[small[i]]+" "+myArr[i]+" "+myArr[big[i]]);
			}
		}
	}

}
