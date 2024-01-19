package class2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedHashSet;
import java.util.Set;

public class Test1181 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] lines = new String[N];
        for (int i = 0; i < N; i++) {
            lines[i] = br.readLine();
        }
        Arrays.sort(lines, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if (s1.length() > s2.length()) {
                    return 1;
                } else if (s1.length() == s2.length()) {
                    return s1.compareTo(s2);
                } else if (s1.length() < s2.length()) {
                    return -1;
                } else {
                    return 0;
                }
            }
        });
        Set<String> linkedHashSetStrList = new LinkedHashSet<>(Arrays.asList(lines));

        String output = linkedHashSetStrList.toString();
        System.out.println(output.substring(1, output.length() - 1).replaceAll(", ", "\n"));
    }
}
