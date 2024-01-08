package class1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test2675 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String[] line = br.readLine().split(" ");
            String[] word = line[1].trim().split("");
            String result = "";
            for (String element : word) {
                result += element.repeat(Integer.parseInt(line[0]));
            }
            System.out.println(result);
        }

    }
}
