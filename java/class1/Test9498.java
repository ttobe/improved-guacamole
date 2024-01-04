package class1;

import java.io.IOException;
import java.util.Scanner;

public class Test9498 {

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.close();
        if (N >= 90) {
            System.out.println("A");
        } else if (N >= 80) {
            System.out.println("B");
        } else if (N >= 70) {
            System.out.println("C");
        } else if (N >= 60) {
            System.out.println("D");
        } else {
            System.out.println("F");
        }
    }

}
