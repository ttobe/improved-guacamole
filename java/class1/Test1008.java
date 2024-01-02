package class1;

import java.util.Scanner;

class Test1008{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);

        double a=scanner.nextDouble();
        double b=scanner.nextDouble();

        scanner.close();
        System.out.print(a/b);
        return ;
    }
}