import java.util.Stack;

public class RemoveOutermostBracket {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String S="(()())(())";
		String finalS="";
        Stack<Character> myStack = new Stack<Character>();
        
        for(int i=0;i<S.length();i++){
            if(S.charAt(i) == '('){
                if(myStack.empty()){
                    myStack.push(S.charAt(i));
                }
                else {
                    finalS=finalS+S.charAt(i);
                    myStack.push(S.charAt(i));            

                }
            }
            else{
                if(myStack.size()==1){
                    myStack.pop();
                }
                else{                    
                finalS=finalS+S.charAt(i);
                    myStack.pop();
                }
            }
        }
        System.out.println(finalS);
	}

}
