/* Задача 1. №5
 Определить дополнительный массив разрешенных значений. Составить массив из элементов
исходного массива, имеющих неразрешенные значения. Вывести результативный массив на экран */
package com.company;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        /*Разрешенным значением соответсвуют нечетные числа, к не соответствующим
        отнеcем четные числа */
        int n;
        System.out.println("Введите размер массива :"); //определяем размер для массива
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        int[] ms =new int[n];
        for(int i=0; i<n; i++)
            ms[i]=((char) (Math.random()*20)); //заполняем массив случайными числами
        System.out.println("Сгенерированный массив :");

        for(int i=0;i<n;i++) {
            System.out.println(ms[i]);
        }

        int k = 0;
        for(int i = 0; i<n; i++) //Определаем количество четных чисел, для выделения места
            if (ms[i] % 2==0) {
                k++;
            }

        System.out.println("Результат :");
        int[] ms1 =new int[k]; //Созадем массив для четных чисел
        k = 0;
        for(int i=0; i<n; i++)
            if (ms[i] % 2==0){
                ms1[k] = ms[i];
                k++;
            }
        for(int i=0;i<k;i++)
            System.out.println(ms1[i]);
    }
}

