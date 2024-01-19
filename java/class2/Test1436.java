package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test1436 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int cnt = 0;
        int i = 0;
        while (cnt < N) {
            i++;
            String str = String.valueOf(i);
            if (str.contains("666")) {
                cnt++;
            }
        }
        System.out.println(i);
    }
}
