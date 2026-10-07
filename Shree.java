import java.util.Scanner;
class Shree {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("enter the number you want to check for palindrome:");
            int org_num = sc.nextInt();
            int num = org_num;
            int rverse = 0;

            while (num != 0) {
                int digit = num % 10;
                rverse = rverse * 10 + digit;
                num = num / 10;
            }

            if (org_num == rverse) {
                System.out.println("number is palindrome");
            } else {
                System.out.println("number is not palindrome");
            }
        }
    }
}
