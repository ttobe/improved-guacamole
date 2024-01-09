package class1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test1157 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] result = new int[26];
        String line = br.readLine().trim().toUpperCase();
        for (int i = 0; i < line.length(); i++) {
            int index = (int) line.charAt(i) - 65;
            result[index]++;
        }
        int max = 0;
        int match = 0;
        int maxIndex = 0;
        for (int i = 0; i < result.length; i++) {
            if (result[i] > max) {
                max = result[i];
                match = 0;
                maxIndex = i;
            } else if (result[i] == max) {
                match++;
            }
        }
        if (match == 0) {
            System.out.println((char) (maxIndex + 65));
        } else {
            System.out.println("?");
        }
    }
}
