//Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.
public class ReverseString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str="i.like.this.program.very.much";
		String[] myChar=str.split("\\.");
		String myString="";
		
		for(int i=myChar.length-1;i>=0;i--) {
			myString+=myChar[i]+".";
		}
		
		System.out.println(myString);
		
	}

}
