import java.io.*;
import java.util.*;

public class Main {
    void bt(int start, ArrayList<Integer> arr, LinkedList<Integer> result, int n) {
        if (result.size() == 6) {
            for (int num : result) {
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }

        for (int i = start; i < n; i++) {
            result.add(arr.get(i));
            bt(i + 1, arr, result, n);
            result.removeLast();
        }
    }

    public static void main(String[] args) throws IOException {
        Main main = new Main();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = br.readLine()) != null) {
            StringTokenizer st = new StringTokenizer(line);
            int n = Integer.parseInt(st.nextToken());
            if (n == 0) break;

            ArrayList<Integer> arr = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                arr.add(Integer.valueOf(st.nextToken()));
            }

            LinkedList<Integer> res = new LinkedList<>();
            main.bt(0, arr, res, n);
            System.out.println();
        }
    }
}
