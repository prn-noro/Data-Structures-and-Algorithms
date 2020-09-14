//Given a string S, find length of the longest substring with all distinct characters.
//For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.
//Input : abababcdefababcdab
//Output : 6 (abcdef)

//Wrong Code
public class LongestDistinctCharacters {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String s="abababcdefababcdab";
		int maxCount=0;
		int localCount;
		for(int i=0;i<s.length();i++) {
			for(int j=i+1;j<s.length();j++) {
				char iChar=s.charAt(i);
				char jChar=s.charAt(j);
				if(iChar==jChar) {
					localCount=j-i;
					System.out.println(localCount);
					if(localCount>maxCount) {
						maxCount=localCount;


					}
					break;
				}
				else {
					continue;
				}
			}
		}
		
		System.out.println(maxCount);

	}

}
