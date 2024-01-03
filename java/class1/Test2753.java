package class1;

import java.io.IOException;
import java.util.Scanner;

public class Test2753 {

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.close();
        if (N % 4 == 0 && (N % 100 != 0 || N % 400 == 0)) {
            System.out.println("1");
            return;
        }
        System.out.println("0");
    }
}
