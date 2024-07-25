import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true){
            int n = sc.nextInt();
            boolean bol = true;
            if(n == 0){
                break;
            }else{
                int cnt = 0;
                String str = Integer.toString(n);
                for(int i=0;i<str.length()/2;i++){
                    if(str.charAt(i) == str.charAt(str.length()-i-1)){
                        continue;
                    }else{
                        bol = false;
                        break;
                    }
                }
                if(bol){
                    System.out.println("yes");
                }else{
                    System.out.println("no");
                }
            }
        }
        sc.close();
    }
}