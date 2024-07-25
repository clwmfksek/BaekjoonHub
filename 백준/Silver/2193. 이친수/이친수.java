import java.util.*;
public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        long arr[] = new long[n+1];
        Arrays.fill(arr,0);
        arr[1] = 1;
        for(int i=2;i<n+1;i++){
            arr[i] = arr[i-2] + arr[i-1];
        }
        System.out.println(arr[n]);
        sc.close();
    }
}