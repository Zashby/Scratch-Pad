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
public class FibSequence {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
      // input to print Fibonacci series

      log("Enter the number you want the Fibonacci series to stop at: ");

      int number = new Scanner(System.in).nextInt();

      log("\nFibonacci number at location " + number + " is ==> " + 
                 (fibonacciLoop(number) + ""));

   }

   //Java program for Fibonacci number
   public static int fibonacciLoop(int number) {
      if (number == 1 || number == 2) {
         return 1;
      }

      int fiba = 1, fibb = 1, fibonacci = 1;
      System.out.println(fiba);
      System.out.println(fibb);
      for (int i = 3; i <= number; i++) {
         fibonacci = fiba + fibb; // Fibonacci number is sum of previous two Fibonacci numbers
         fiba = fibb;
         fibb = fibonacci;
         if(fibb > number) break;
         System.out.println(fibb);
         }
      return fibonacci; // Fibonacci number
      
   }

   private static void log(String number) {
      System.out.println(number);

   }
}
