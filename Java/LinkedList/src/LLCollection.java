import java.util.*;

public class LLCollection {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			List<Integer> ll=new LinkedList<Integer>();
			
			ll.add(1);
			ll.add(2);
			ll.add(3);
			ll.add(0,0);
			ll.add(4,4);
			ll.remove(4);
			ll.remove(2);
			ll.set(0, 100);
			System.out.println(ll);
	}

}
