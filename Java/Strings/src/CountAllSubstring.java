import java.util.*;
public class CountAllSubstring {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s="abcd";
		Set <String> mySet=new HashSet<String>();
		ArrayList<String> myList=new ArrayList<String>();
		
		
		for(int i=0;i<s.length();i++) {
			for(int j=i;j<s.length();j++) {
				String result=s.substring(i,j+1);
				myList.add(result);
			}
		}
		for(String k:myList) {
			System.out.println(k);
		}
	}

}
