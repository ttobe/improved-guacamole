package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Test4949 {

    public static String reg = "[\\(\\)\\[\\]]";

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        while (true) {
            String line = br.readLine();
            if (line.equals(".")) {
                break;
            }
            String[] lines = line.split("");
            Stack<String> stack = new Stack<>();
            for (String word : lines) {
                switch (word) {
                    case ("("):
                    case ("["):
                        stack.push(word);
                        break;
                    case (")"):
                        if (!stack.isEmpty() && stack.peek().equals("(")) {
                            stack.pop();
                        } else {
                            stack.push(")");
                        }
                        break;
                    case ("]"):
                        if (!stack.isEmpty() && stack.peek().equals("[")) {
                            stack.pop();
                        } else {
                            stack.push("]");
                        }
                        break;
                }
            }
            if (stack.empty()) {
                sb.append("yes\n");
            } else {
                sb.append("no\n");
            }

        }
        System.out.println(sb);

    }
}
