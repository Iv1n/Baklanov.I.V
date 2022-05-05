package FourthWork;

import Opis1.Opis1_1;

public class Xrupkost extends Opis1_1 {

    private double fragilityFactor;

    public Xrupkost(long id, int productCode, String name, int wholesalePrice, int retailPrice, String description, double fragilityFactor) {
        super(id, productCode, name, wholesalePrice, retailPrice, description);
        this.fragilityFactor = fragilityFactor;
    }

    public double getFragilityFactor() {
        return fragilityFactor;
    }

    public void setFragilityFactor(double fragilityFactor) {
        this.fragilityFactor = fragilityFactor;
    }

    public String toString() {
        return "\n" + super.toString() +
                "\n Коэффициент хрупкости - " + fragilityFactor;
    }


}