import java.util.*; 
public class Timepass
{
	public static void main(String[] args) {
		

        HashSet<Integer> h = new HashSet<>(); 
        int val=0;
        // Adding elements into HashSet usind add() 
        h.add(1); 
        h.add(2); 
        h.add(3); 
  
        // Iterating over hash set items 
        Iterator<Integer> i = h.iterator(); 
        while (i.hasNext()) 
            val+=i.next(); 
            System.out.println(val);

	}
}