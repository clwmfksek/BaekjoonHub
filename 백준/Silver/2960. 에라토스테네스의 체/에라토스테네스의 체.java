import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        ArrayList<Integer> list = new ArrayList<>();

        for(int i = 2; i <= n; i++){
            list.add(i);
        }
        int cnt = 0;
        for(int i=0;i<n;i++) {
            int num = list.get(0);
            for (int j = 0; j < list.size(); j++) {
                if (list.get(j) % num == 0) {
                    cnt++;
                    if(cnt==k){
                        System.out.println(list.get(j));
                        return;
                    }
                    list.remove(j);
                    j--;
                }
            }
        }
    }
}
