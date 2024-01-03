package class1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test2475 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = 0;
        String[] str = br.readLine().split(" ");
        for (String e : str) {
            int tmp = Integer.parseInt(e);
            sum += tmp * tmp;
        }
        System.out.println(sum % 10);
    }
}
