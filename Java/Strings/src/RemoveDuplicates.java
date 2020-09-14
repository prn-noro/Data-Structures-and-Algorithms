import java.util.HashSet;

//Given a string, the task is to remove duplicates from it.
//Expected time complexity O(n) where n is length of input string
//under the assumption that there are total 256 possible characters in a string.
public class RemoveDuplicates {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s="geeks for geeks";
//		Output:geksfor
		HashSet<Character> mySet =new HashSet<Character>();
		String myS="";
		
		for(int i=0;i<s.length();i++) {
			char myChar=s.charAt(i);
			if(!mySet.contains(myChar)) {
				myS+=myChar;
				mySet.add(myChar);
			}
		}
		
		System.out.println(myS);
	}

}
