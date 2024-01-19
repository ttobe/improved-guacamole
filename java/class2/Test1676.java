package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Test1676 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        BigInteger bigNumber1 = new BigInteger(String.valueOf(1));
        for (int i = 1; i <= N; i++) {
            bigNumber1 = bigNumber1.multiply(BigInteger.valueOf(i));
        }
        String str = String.valueOf(bigNumber1);
        int cnt = 0;
        for (int i = str.length() - 1; i > 0; i--) {
            if (str.charAt(i) != '0') {
                break;
            }
            cnt++;
        }
        System.out.println(cnt);
    }


}
