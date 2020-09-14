//Find majority element in array. Majority element is that element which occurs more than n/2 times
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
public class FindMajority {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int myArr[]= {3,1,3,3,2,4,5,5,5,5,5,5,5,5};
		List<Integer> myList = new ArrayList<Integer>();
		HashMap<Integer,Integer> myMap=new HashMap<Integer,Integer>();
		int myLen=myArr.length;
		
		for(int i=0;i<myArr.length;i++) {
			if(!myMap.containsKey(myArr[i])) {
				myMap.put(myArr[i],1);
			}
			else {
				myMap.put(myArr[i],myMap.get(myArr[i])+1);
				if(myMap.get(myArr[i])>myLen/2){
					myList.add(myArr[i]);
				}
			}
		}
		
		System.out.println(myList);
		
	}

}
