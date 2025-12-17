import java.io.*;
import java.util.*;

public class 듣보잡1764 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            set.add(br.readLine());
        }

        ArrayList<String> ans = new ArrayList<String>();
        for (int i = 0; i < m; i++) {
            String str = br.readLine();
            if (set.contains(str)) {
                ans.add(str);
            }
        }

        Collections.sort(ans);

        bw.write(ans.size() + "\n");
        for (String s : ans) {
            bw.write(s + "\n");
        }

        br.close();
        bw.close();
    }
}