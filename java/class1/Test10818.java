package class1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test10818 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int min = 1000000;
        int max = -1000000;
        String[] str = br.readLine().split(" ");
        for (String e : str) {
            int tmp = Integer.parseInt(e);
            if (tmp < min) {
                min = tmp;
            }
            if (tmp > max) {
                max = tmp;
            }
        }
        System.out.println(min + " " + max);
    }
}
