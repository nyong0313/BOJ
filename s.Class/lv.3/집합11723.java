import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class 집합11723 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int m = Integer.parseInt(br.readLine());
        boolean s[] = new boolean[21];

        for (int i = 0; i < m; i++) {
            String[] input = br.readLine().split(" ");
            String cmd = input[0];
            int num = input.length > 1 ? Integer.parseInt(input[1]) : 0;

            switch (cmd) {
                case "add":
                    s[num] = true;
                    break;
                case "remove":
                    s[num] = false;
                    break;
                case "check":
                    if (s[num])
                        bw.write("1\n");
                    else
                        bw.write("0\n");
                    break;
                case "toggle":
                    if (s[num])
                        s[num] = false;
                    else
                        s[num] = true;
                    break;
                case "all":
                    Arrays.fill(s, true);
                    break;
                case "empty":
                    Arrays.fill(s, false);
                    break;
            }
        }

        br.close();
        bw.close();
    }
}