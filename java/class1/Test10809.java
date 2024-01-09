package class1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Test10809 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] result = new int[26];
        Arrays.fill(result, -1);
        String line = br.readLine().trim();
        for (int i = 0; i < line.length(); i++) {
            int index = (int) line.charAt(i) - 97;
            if (result[index] == -1) {
                result[index] = i;
            }
        }

        for (int element : result) {
            System.out.print(element + " ");
        }

    }
}
