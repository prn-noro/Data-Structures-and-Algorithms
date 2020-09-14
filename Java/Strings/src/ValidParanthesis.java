import java.util.HashSet;
import java.util.Stack;

public class ValidParanthesis {

    public boolean isValid(String s) {
        HashSet<Character> mySet = new HashSet<Character>();
        Stack<Character> myStack=new Stack<Character>();
        mySet.add('(');
        mySet.add('{');
        mySet.add('[');
        for(int i=0;i<s.length();i++){
            char myChar=s.charAt(i);
            if(mySet.contains(myChar)){
                myStack.push(myChar);
            }
            else{
                if(myStack.size()==0){
                    return false;
                }
                if(myChar==')' && myStack.lastElement()!='('){
                    return false;
                }
                else if(myChar==']' && myStack.lastElement()!='['){
                    return false;
                }
                if(myChar=='}' && myStack.lastElement()!='{'){
                    return false;
                }
                myStack.pop();
            }
        }
        if(myStack.empty()){
            return true;
        }
        return false;
    }
}