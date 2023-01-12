/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

import java.util.Scanner;

/**
 *
 * @author Marvine_2
 */
public class FibSequence2 {

    /**
     * @param args the command line arguments
     */
    
    public static void main(String[] args) {
      // input to print Fibonacci series

      log("Enter the number you want the Fibonacci series to stop at: ");

      int number = new Scanner(System.in).nextInt();

      log("\nUsing recursion, the number to stop at is " + number);
      for (int i=1; i <= number; i++) {
          if(fibonacciRecursion(i) > number) break;
          log(fibonacciRecursion(i) + " ");
      }
      
    }
      
    public static int fibonacciRecursion(int number) {
        if (number == 1 || number == 2) {
            return 1;
        }

        return fibonacciRecursion(number - 1) + fibonacciRecursion(number - 2);
    }

    private static void log(String number) {
        System.out.println(number);   
    }

}