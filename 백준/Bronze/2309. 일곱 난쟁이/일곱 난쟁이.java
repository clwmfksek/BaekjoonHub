import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] li = new int[9];
        int sum = 0;
        int a = 0,b = 0;
        for(int i=0;i<9;i++) {
            li[i] = (sc.nextInt());
            sum += li[i];
        }
        Arrays.sort(li);

        for(int i=0;i<8;i++){
            for(int j=i+1;j<9;j++){
                if(sum - li[i] - li[j] == 100){
                    a = i;
                    b = j;
                    break;
                }
                    }
                }
        for(int k = 0; k< li.length;k++){
            if(k!=a && k!=b) {
                System.out.println(li[k]);
            }
        }
    }
}