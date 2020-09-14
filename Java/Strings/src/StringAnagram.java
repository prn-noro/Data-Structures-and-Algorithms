import java.util.HashMap;

class StringAnagram {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> myMap1= new HashMap<Character,Integer>();
        HashMap<Character,Integer> myMap2= new HashMap<Character,Integer>();
        
        for(int i=0;i<s.length();i++){
            if(!myMap1.containsKey(s.charAt(i))){
                myMap1.put(s.charAt(i),1);
            }
            else{
                myMap1.put(s.charAt(i),myMap1.get(s.charAt(i))+1);
            }
        }
        for(int i=0;i<t.length();i++){
            if(!myMap2.containsKey(t.charAt(i))){
                myMap2.put(t.charAt(i),1);
            }
            else{
                myMap2.put(t.charAt(i),myMap2.get(t.charAt(i))+1);
            }
        }
        if(myMap1.equals(myMap2)){
            return true;
        }
        return false;
    }
}