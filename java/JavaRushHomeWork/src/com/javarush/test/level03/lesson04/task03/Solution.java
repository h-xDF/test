package com.javarush.test.level03.lesson04.task03;

/* StarCraft
Создать 10 зергов, 5 протосов и 12 терран.
Дать им всем уникальные имена.
*/

public class Solution
{
    public static void main(String[] args)
    {
        //напишите тут ваш говнокод
        Zerg[] zergArr = new Zerg[10];
        Protos[] protosArr = new Protos[5];
        Terran[] terranArr = new Terran[15];

        for (int i = 0; i < 10; i++) {
            zergArr[i] = new Zerg();
            zergArr[i].name = "zrya" + i;
        }

        for (int i = 0; i < 5; i++) {
            protosArr[i] = new Protos();
            protosArr[i].name = "tos" + i;
        }

        for (int i = 0; i < 12; i++) {
            terranArr[i] = new Terran();
            terranArr[i].name = "Shepart" + i;
        }

        for(int i = 0; i < 10; i++){
            System.out.println(zergArr[i].name);
        }

        for (int i = 0; i < 5; i++){
            System.out.println(protosArr[i].name);
        }

        for (int i = 0; i < 12; i++){
            System.out.println(terranArr[i].name);
        }
        // таким же макаром остальные жители славной игры
//        Zerg one = new Zerg();
//        one.name = "123";
//        Zerg two = new Zerg();
//        two.name = "321";
//        System.out.println("name two Zerg  " + two.name);
//        System.out.println("name Zerg  " + one.name);


        //напи

    }

    public static class Zerg
    {
        public String name;
    }

    public static class Protos
    {
        public String name;
    }

    public static class Terran
    {
        public String name;
    }
}