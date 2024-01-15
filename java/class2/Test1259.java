package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test1259 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String N = br.readLine().trim();
            if (N.equals("0")) {
                break;
            }
            boolean flag = false;
            String[] line = N.split("");
            int length = line.length;

            for (int i = 0; i < length / 2; i++) {
                if (!line[i].equals(line[length - 1 - i])) {
                    flag = true;
                }
            }

            if (flag) {
                System.out.println("no");

            } else {
                System.out.println("yes");
            }

        }

    }
}
