import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        int sum = 0;
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        ArrayList<Integer> li = new ArrayList<>();
        ArrayList<Integer> li2 = new ArrayList<>();
        ArrayList<Integer> li3 = new ArrayList<>();
        for(int i = 0;i<N;i++){
            li.add(sc.nextInt());
        }
        for(int i=0;i<N;i++){
            li2.add(sc.nextInt());
        }
        for(int i=0;i<N;i++){
            li3.add(Collections.max(li2) * Collections.min(li));
            li2.remove(Collections.max(li2));
            li.remove(Collections.min(li));
            }
        for(int i=0;i<N;i++){
            sum += li3.get(i);
        }
        System.out.println(sum);
        }

    }
