/* №2 Вариант 5
  Дан массив b (n) . Переписать в массив C(n) положительные элементы
массива b(n) деленные на 5. (со сжатием., без пустых элементов внутри). Затем
упорядочить методом «выбора и перестановки» по возрастанию новый массив.  */
package com.company;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n;
        int a = -20;
        int t = 50;
        System.out.println("Введите размер массива :"); //определяем размер для массива
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        int[] b = new int[n];

        for (int i = 0; i < n; i++)
            b[i] = (a + (int) (Math.random() * t)); //заполняем массив случайными числами
        System.out.println("массив B:");
        for (int i = 0; i < n; i++) //Выводим сгенерированынй массив
            System.out.println(b[i]);

        int l = 0; //Считаем количесвто положительных массивов для выделения места
        for (int i = 0; i < n; i++) {
            if (b[i] > 0) {
                l++;
            }
        }
        int k=0;
        int[] c = new int[l]; //Создаем новый массив для положительных чисел
        for (int i = 0; i < n; i++) {  //Заполняем массив
            if (b[i] > 0) {
                c[k] = b[i];
                k++;
            }
        }

        for (int i = 0; i < k; i++) {  //Делим на 5
            c[i] = c[i] / 5;
        }

        for (int i = 0; i < k-1; i++) {    //сортировка
            int m = i;
            int min = c[i];
            for (int j = i + 1; j < k; j++)
                if (c[j] < min) {
                    m = j;
                    min = c[j];
                }
            c[m]=c[i];
            c[i]=min;
        }

        System.out.println("Массив C :");   //вывод отсортированного массива
        for (int i = 0; i < c.length; i++)
            System.out.println(c[i]);

    }

}
