import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int p = sc.nextInt();
        ArrayList<Integer> list = new ArrayList<>();
        if(n>0){
            for(int i = 0; i < n; i++){
                list.add(sc.nextInt());
            }
            list.add(m);
            list.sort(Comparator.reverseOrder());
            if(list.get(list.size()-1)==m){
                if(list.size() > p){
                    System.out.println(-1);
                }
                else{
                    System.out.println(list.indexOf(m)+1);
                }
            }
            else {
                list.remove(list.size() - 1);
                if (list.size() > p) {
                    System.out.println(-1);
                } else {
                    System.out.println(list.indexOf(m) + 1);
                }
            }
        }
        else{
            System.out.println(1);
        }
    }
}
