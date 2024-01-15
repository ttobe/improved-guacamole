package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Test1546 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] line = br.readLine().split(" ");
        int[] scores = new int[line.length];

        for (int i = 0; i < line.length; i++) {
            scores[i] = Integer.parseInt(line[i]);
        }
        double sum = Arrays.stream(scores).sum();
        double max = Arrays.stream(scores).max().getAsInt();

        System.out.println((sum / Double.valueOf(line.length)) / max * 100);


    }
}
