/* Вариант 5
Реализация готовой продукции. Создать родительский класс «Товар»
(идентификатор, код, наименование, цена, описание) и дочерние классы:
 «Хрупкий товар» (коэффициент хрупкости);
 «Скоропортящийся товар» (мах время хранения);
 «Габаритный товар» (высота, ширина, длина).
Реализовать класс для хранения списка товаров с методом добавления нового
товара и методом печати списка товаров. */

package FourthWork;

import Opis1.Opis1_1;

import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {

        ArrayList<Opis1_1> listOfCommodities = new ArrayList<>();
        CommodityList commodityList = new CommodityList(listOfCommodities);

        long cupId = 1;
        int cupProductCode = 1202_01;
        String cupName = "Кружка";
        int cupWholesalePrice = 350;
        int cupRetailPrice = 525;
        String cupDescription = "Большая белая кружка с изображением собакена";
        double cupFragilityFactor = 0.38;

        Xrupkost glass = new Xrupkost(cupId, cupProductCode, cupName, cupWholesalePrice, cupRetailPrice, cupDescription, cupFragilityFactor);

        commodityList.addCommodity(glass);

        long kvassId = 2;
        int kvassProductCode = 126;
        String kvassName = "Квас";
        int kvassWholesalePrice = 18;
        int kvassRetailPrice = 27;
        String kvassDescription = "Темный, вкусный, холодный - все что нужно в теплый летний день";
        double kvassStorageTime = 36;
        time kvass = new time(kvassId, kvassProductCode, kvassName, kvassWholesalePrice, kvassRetailPrice, kvassDescription, kvassStorageTime);

        commodityList.addCommodity(kvass);

        long boxId = 3;
        int boxProductCode = 16_412;
        String boxName = "Коробка для вещей ";
        int boxWholesalePrice = 1200;
        int boxRetailPrice = 2000;
        String boxDescription = "Отличная коробка";
        double boxHeight = 1;
        double boxWidth = 0.8;
        double boxLength = 0.6;
        Gaboriti box = new Gaboriti(boxId, boxProductCode, boxName, boxWholesalePrice, boxRetailPrice, boxDescription, boxHeight, boxLength, boxWidth);

        commodityList.addCommodity(box);

        System.out.println(commodityList.showCommodities());

    }

}
