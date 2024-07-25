import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for(int i=0;i<t;i++){
            int n = Integer.parseInt(br.readLine());
            long []dp = {10,9,8,7,6,5,4,3,2,1};

            for(int j=0;j<n-1;j++){
                for(int k=0;k<10;k++){
                    for(int l=k+1;l<10;l++){
                        dp[k] += dp[l];
                    }
                }
            }
            System.out.println(dp[0]);
        }
    }    
}
