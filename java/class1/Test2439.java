package class1;

import java.io.IOException;
import java.util.Scanner;

public class Test2439 {

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.close();
        for (int i = 1; i <= N; i++) {
            System.out.println(" ".repeat(N - i) + "*".repeat(i));
        }
    }
}
