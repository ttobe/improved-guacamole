package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test2869 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int A = Integer.parseInt(line[0]);
        int B = Integer.parseInt(line[1]);
        int V = Integer.parseInt(line[2]);

        int day = (V - B) / (A - B);
        if ((V - B) % (A - B) != 0) {
            day++;
        }
        System.out.println(day);


    }
}
