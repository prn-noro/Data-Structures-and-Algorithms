
public class LongestPalindrome {

	
	static boolean isPalindrome(String s) {
		char tempArr[]=s.toCharArray();
		String reverseS="";
		for(int i=tempArr.length-1;i>=0;i--) {
			reverseS+=tempArr[i];
		}
		
		if(s.equals(reverseS)) {

			return true;
		}
		else{
			return false;
		}
	}
	public static void main(String [] args) {
		String s="aaaabbaa";
		int maxLength=0;
		String maxString=""; 
		for(int i=0;i<s.length();i++) {
			int left=i;
			int right=s.length()-1;
			while(left<right) {
				String myString=s.substring(left,right+1);
				right-=1;
				if(isPalindrome(myString)) {
					if (myString.length() >maxLength) {
						maxString=myString;
						maxLength=myString.length();
					}
				}
			}
		}
		
		System.out.println(maxString);
	}
}
