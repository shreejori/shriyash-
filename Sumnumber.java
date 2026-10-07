import java.util.Scanner;

class SumNumbers
{
    public static void main(String args[])
    {
        try (Scanner sc = new Scanner(System.in))
        {
            System.out.print("Enter how many numbers: ");
            int n = sc.nextInt();

            int sum = 0;

            for (int i = 1; i <= n; i++)
            {
                System.out.print("Enter number:");
                int num = sc.nextInt();
                sum += num;
            }

            System.out.println("Sum = " + sum);
        }
    }
}