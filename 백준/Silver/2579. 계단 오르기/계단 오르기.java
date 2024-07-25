import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        // 계단 점수
        int[] step = new int[N+1];
        // 각 계단까지 오를 때 최대 점수
        int[] dp = new int[N+1];

        for (int i=1;i<=N;i++) {
            step[i]= sc.nextInt();
        }

        // dp 값 구하기
        dp[1] = step[1];
        if (N>=2) {
            dp[2] = step[1] + step[2];
        }
        /*
        * X번째 계단으로 가는 방법
        * 1. 두 칸 전 계단에서 오르기
        * 2. 한 칸 전 계단에서 오르기 (세 계단 전 -> 한 계단 전-> 현재)
        */
        for (int X=3;X<=N;X++) {
            dp[X] = step[X] + Math.max(dp[X-2],dp[X-3]+step[X-1]);
        }
        System.out.println(dp[N]);
    }
}
