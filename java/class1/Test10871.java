package class1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test10871 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");
        int X = Integer.parseInt(str[1]);

        str = br.readLine().split(" ");
        for (String e : str) {
            if (Integer.parseInt(e) < X) {
                System.out.print(e + " ");
            }
        }
    }
}
