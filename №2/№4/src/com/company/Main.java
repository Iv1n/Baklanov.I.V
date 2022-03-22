/* №4 Вариант 5
 Дан двумерный массив A, размером (nn) (или квадратная матрица A).
Найти количество положительных элементов её главной диагонали. Затем умножить
побочную диагональ на найденное количество */
package com.company;

import java.util.Scanner;
import java.util.Random;
public class Main {

    public static void main(String[] args) {
        int n;
        System.out.println("Введите размер массива :"); //определяем размер для массива
        Scanner in = new Scanner(System.in);
        n = in.nextInt();

        int[][] a = new int[n][n]; //Выделяем место для матрицы
        int k = 50;
        int p = 0;
        int len = a.length;
        Random random = new Random();
        System.out.println("Матрица:");

        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                int u = -9 + random.nextInt(k); //заполняем матрицу
                a[i][j] = u;
                System.out.print(a[i][j] + " ");
                if (i == j && u > 0) {  //находим количество положительных элеметнов главной диагонали
                    p++;
                }
            }
            System.out.println();
        }
        System.out.println("Количество положительных элементов главной диагонали = " + p);
        System.out.println("Преобразованная матрица :");

        for (int i = 0; i < len; i++) {  //Выводим преобразованную матрицу
            a[i][len - 1 - i] *= p;
            for (int j = 0; j < len; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }
    }
}
