import java.util.Arrays;
import java.util.Scanner;

public class 소수찾기1978 {
    public static void main(String[] args) {
        boolean prime[] = new boolean[1001];
        Arrays.fill(prime, true);

        prime[1] = false;
        for (int i = 2; i < (int) Math.sqrt(1001) + 1; i++) {
            if (prime[i]) {
                for (int j = i + i; j < 1001; j += i) {
                    prime[j] = false;
                }
            }
        }

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int a[] = new int[n];
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
            if (prime[a[i]]) {
                cnt++;
            }
        }

        System.out.println(cnt);

        sc.close();
    }
}