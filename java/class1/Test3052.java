package class1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Test3052 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> results = new ArrayList<Integer>(10);
        int count = 0;
        for (int i = 0; i < 10; i++) {
            Integer N = Integer.parseInt(br.readLine().trim());
            if (!results.contains(N % 42)) {
                count++;
                results.add(N % 42);
            }
        }
        System.out.println(count);

    }
}
