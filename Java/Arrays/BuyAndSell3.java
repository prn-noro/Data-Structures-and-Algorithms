//Incorrect
import java.util.ArrayList;
import java.util.Collections;

public class BuyAndSell3 {
	 public static void maxProfit(int[] prices) {
	        ArrayList<Integer> myList = new ArrayList<Integer>();
	        int bought=0;
	        int buyPrice=0;
	        int sellPrice=0;
	        int maxProfit=0;
	        for(int i=0;i<prices.length-1;i++){
	            if(prices[i]<=prices[i+1] && bought==0){
	                buyPrice=prices[i];
	                bought=1;
	            }
	            else if(prices[i]>prices[i+1] && bought==1){
	                sellPrice=prices[i];
	                maxProfit=sellPrice-buyPrice;
	                myList.add(maxProfit);
	                bought=0;
	            }
	            if(i==prices.length-2 && bought==1){
	                sellPrice=prices[i+1];
	                maxProfit=sellPrice-buyPrice;
	                myList.add(maxProfit);
	                bought=0;
	            }
	        }
	        System.out.println(myList);
	        Collections.sort(myList);
	        int maxReturn=myList.get(myList.size()-1)+myList.get(myList.size()-2);
	        System.out.println(maxReturn);
	        
	    }
	 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int myArr[]= {1,2,3,4,5};
		maxProfit(myArr);
		
	}

}