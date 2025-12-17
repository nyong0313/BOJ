import java.util.Scanner;

public class 직각삼각형4153 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int A[] = new int[3];
            int max = 0;
            int maxi = 0;
            for (int i = 0; i < 3; i++) {
                A[i] = sc.nextInt();
                if (max < A[i]) {
                    max = A[i];
                    maxi = i;
                }
            }

            if (max == 0)
                break;

            if (max * max == A[(maxi + 1) % 3] * A[(maxi + 1) % 3] + A[(maxi + 2) % 3] * A[(maxi + 2) % 3]) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }

        sc.close();
    }
}