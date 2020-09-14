import java.util.*;
public class BurialTreasure {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int finalArr[]= {0,0};
		String artifacts="1B 2C, 2D 4D";
		String searched="2B 2D 3B 3D 4A";
		HashSet<String> mySet=new HashSet<String>();
		
		String myArr[]=artifacts.split(",");
		
		for(String i:myArr) {
			System.out.println(i);
		}
	}

}
