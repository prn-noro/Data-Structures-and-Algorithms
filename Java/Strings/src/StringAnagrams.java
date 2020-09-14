import java.util.HashMap;
public class StringAnagrams {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s1="geeksforgeeks";
		String s2="forgeeksgeekss";
		HashMap<Character,Integer> myMap1=new HashMap<Character,Integer>();
		HashMap<Character,Integer> myMap2=new HashMap<Character,Integer>();
		
		for(int i=0;i<s1.length();i++) {
			char myChar=s1.charAt(i);
			if(myMap1.containsKey(myChar)) {
				myMap1.put(myChar,myMap1.get(myChar)+1);
			}
			else {
				myMap1.put(myChar,1);
			}	
		}
		for(int i=0;i<s2.length();i++) {
			char myChar=s2.charAt(i);
			if(myMap2.containsKey(myChar)) {
				myMap2.put(myChar,myMap2.get(myChar)+1);
			}
			else {
				myMap2.put(myChar,1);
			}	
		}
		
		if(myMap1.equals(myMap2)) {
			System.out.println("String Anagrams");
		}
		else {
			System.out.println("Not String Anagrams");
		}
		
	}

}
