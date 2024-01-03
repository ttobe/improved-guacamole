package class1;

import java.util.Scanner;

public class Test2438 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.close();

        for (int i = 1; i <= N; i++) {
            System.out.println("*".repeat(i));
        }
    }

}
