package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test2839 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        // 5로 나누고 나머지를 3으로 가져갈 수 있는가?
        // 그 이후에 + 5를 하고 3ㅡ로  가져갈 수 있음?

        int five = N / 5;
        int rest = N % 5;

        int result = 0;
        while (five > -1) {
            if (rest % 3 == 0) {
                result = five + rest / 3;
                break;
            } else {
                five--;
                rest += 5;
            }
        }
        if (result == 0) {
            System.out.println("-1");
        } else {
            System.out.println(result);
        }

    }
}
