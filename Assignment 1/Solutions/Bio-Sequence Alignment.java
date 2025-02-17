import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        for (int testCase = 0; testCase < t; testCase++) {

            int length = scanner.nextInt();
            scanner.nextLine(); 
            String[] num = scanner.nextLine().split(" ");
            int sample = scanner.nextInt();
            scanner.nextLine(); 
            
            for (int s = 0; s < sample; s++) {

                String DNA = scanner.nextLine();
                boolean match = true;
                HashMap<String, Character> pair = new HashMap<>();
                
                if (DNA.length() != length) {

                    System.out.println("NO");
                    continue;
                }
                
                for (int i = 0; i < length; i++) {
                    
                    String currentNum = num[i];
                    char currentChar = DNA.charAt(i);
                    
                    if (!pair.containsKey(currentNum)) {
                        if (pair.containsValue(currentChar)) {
                            match = false;
                            break;
                        }
                        pair.put(currentNum, currentChar);
                    } else {
                        if (pair.get(currentNum) != currentChar) {
                            match = false;
                            break;
                        }
                    }
                }
                
                System.out.println(match ? "YES" : "NO");
            }
        }
        scanner.close();
    }
}
