package class1;

import java.io.IOException;
import java.util.Scanner;

public class Test2562 {

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int max = 0;
        int maxIndex = 0;
        for (int i = 1; i <= 9; i++) {
            int N = scanner.nextInt();
            if (max < N) {
                max = N;
                maxIndex = i;
            }
        }
        System.out.println(max);
        System.out.println(maxIndex);
    }

}
