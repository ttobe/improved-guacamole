package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Test2775 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int[][] arr = new int[15][15];
        Arrays.setAll(arr[0], num -> (num + 1));
//        System.out.println(Arrays.toString(arr[0]));
        for (int i = 1; i < 15; i++) {
            arr[i][0] = arr[i - 1][0];
            for (int j = 1; j < 15; j++) {
                arr[i][j] = arr[i][j - 1] + arr[i - 1][j];
            }
        }

        for (int i = 0; i < T; i++) {
            int k = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());
            System.out.println(arr[k][n - 1]);
        }


    }
}
