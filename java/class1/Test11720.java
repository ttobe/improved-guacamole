package class1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test11720 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int sum = 0;
        String[] str = br.readLine().split("");
        for (String e : str) {
            sum += Integer.parseInt(e);
        }
        System.out.println(sum);
    }
}
