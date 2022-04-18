package com.company;


public class Main {
    public static void main(String[] args) {
        long id = 12;
        int productCode = 321;
        String name = "Смартфон Honor 10 Lite";
        int wholesalePrice = 9300;
        int retailPrice = 16700;
        String description = "Смартфон Honor 10 lite черного цвета, 3GB RAM, 32GB, micro-usb";
        dabl exampleObject = new dabl(id, productCode, name, wholesalePrice, retailPrice, description);
        System.out.println(exampleObject);
    }

}
