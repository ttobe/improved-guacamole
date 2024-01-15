package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test2798 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().trim().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);

        int[] cards = new int[N];
        String[] tmp = br.readLine().trim().split(" ");
        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(tmp[i]);
        }
        int assumption = 0;

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                for (int k = j + 1; k < N; k++) {
                    int nowSum = cards[i] + cards[j] + cards[k];
                    if (assumption < nowSum && nowSum <= M) {
                        assumption = nowSum;
                    }
                }
            }
        }
        System.out.println(assumption);
    }
}
