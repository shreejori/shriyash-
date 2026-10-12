import java.util.Scanner;
public class prime_number {
    public static void main(String args[]){
        Scanner sc =new Scanner(System.in);
        System.out.println("enter a number");
        int n=sc.nextInt();
        if(n<1){
        System.out.println("invalid");
        }
        else if(n==1){
            System.out.println("no factor");

        
        }
        else{
            for(int i=2;i<=n;i++){
                while (n%i==0) {
                    System.out.println(i+" ");
                       n/=i;
                }
            }
        }
    }
    
}