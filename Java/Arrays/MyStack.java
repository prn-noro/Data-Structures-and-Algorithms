import java.util.Stack;

public class MyStack {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Stack<Integer> myStack = new Stack<Integer>();
		myStack.push(1);
		myStack.push(2);
		myStack.push(3);
		myStack.push(4);
		myStack.push(5);
		System.out.println(myStack.pop());
		System.out.println(myStack.peek());
	}

}
