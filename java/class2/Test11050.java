package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test11050 {

    static int[][] dp = new int[11][11];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int N = Integer.parseInt(line[0]);
        int K = Integer.parseInt(line[1]);
        System.out.println(johab(N, K));
    }

    public static int johab(int n, int k) {
        if (k == 0 || n == k) {
            return 1;
        }
        if (dp[n][k] == 0) {
            dp[n][k] = johab(n - 1, k - 1) + johab(n - 1, k);
        }
        return dp[n][k];
    }

}
