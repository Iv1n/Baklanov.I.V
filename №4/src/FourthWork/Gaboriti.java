package FourthWork;

import Opis1.Opis1_1;

public class Gaboriti extends Opis1_1 {

    private double height;
    private double width;
    private double length;

    public Gaboriti(long id, int productCode, String name, int wholesalePrice, int retailPrice, String description, double height, double length, double width) {
        super(id, productCode, name, wholesalePrice, retailPrice, description);
        this.height = height;
        this.length = length;
        this.width = width;
    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double getWidth() {
        return width;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    public double getHeight() {
        return height;
    }

    public void setHeight(double height) {
        this.height = height;
    }

    public String toString() {
        return "\n" + super.toString() +
                "\n Высота (метры) - " + height +
                "\n Ширина (метры) - " + width +
                "\n Длина (метры) - " + length;
    }


}
