import java.util.Scanner;
class first_questionn{
    public static void main(String[] args) {
        System.out.println("enter your attendance in 1 for present and 0 for absent");
        System.out.println("attendance");

        int p_d = 0;
        int a_d = 0;
        int t_d;

        try (Scanner scanner = new Scanner(System.in)) {
            int attendance = scanner.nextInt();
            if (attendance == 1) {
                System.out.println("present");
                p_d = p_d + 1;
            } else {
                System.out.println("absent");
                a_d = a_d + 1;
            }
            t_d = p_d + a_d;
        }

        float atten_percentage = (p_d * 100.f) / t_d;
        System.out.println("percentage of total present days is  :" + atten_percentage);
    }
}