import java.util.Scanner;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) {
        int sum = 0;
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Integer> li = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            int len = li.size();
            if (num == 0) {
                li.remove(len-1);
            }else{
                li.add(num);
            }
        }
        int len = li.size();
        for (int i = 0; i < len; i++) {
            sum += (int) li.get(i);
        }
        System.out.println(sum);
    }
}