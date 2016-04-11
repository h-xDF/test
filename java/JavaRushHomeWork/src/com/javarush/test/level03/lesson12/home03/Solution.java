package com.javarush.test.level03.lesson12.home03;

/* Я буду зарабатывать $50 в час
Ввести с клавиатуры число n.
Вывести на экран надпись «Я буду зарабатывать $n в час».
Пример:
Я буду зарабатывать $50 в час
*/
import java.io.*;

public class Solution
{
    public static void main(String[] args)   throws Exception
    {
        // 1 вариант
//        InputStream inputStream = System.in;
//        Reader inputStreamReader = new InputStreamReader(inputStream);
//        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
//
//        String name = bufferedReader.readLine(); //читаем строку с клавиатуры
//        String sAge = bufferedReader.readLine(); //читаем строку с клавиатуры
//        int nAge = Integer.parseInt(sAge); //преобразовываем строку в число.
//
        // 2 вариант
//        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
//
//        String name = reader.readLine();
//        String sAge = reader.readLine();
//        int nAge = Integer.parseInt(sAge);


        // 3 варинат
//        Scanner scanner = new Scanner(System.in);
//        String name = scanner.nextLine();
//        int age = scanner.nextInt();

        InputStream inputStream = System.in;
        Reader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);

        String cashe = bufferedReader.readLine();

        System.out.println("Я буду зарабатывать $" + cashe + " в час");


        //напишите тут ваш код

    }
}