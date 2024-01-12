package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test2292 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer N = Integer.parseInt(br.readLine().trim());
        int count = 1; // 겹 수(최소 루트)
        int range = 2;    // 범위 (최솟값 기준)

        if (N == 1) {
            System.out.print(1);
        } else {
            while (range <= N) {    // 범위가 N보다 커지기 직전까지 반복
                range = range + (6 * count);
                count++;
            }
            System.out.print(count);
        }

    }
}
