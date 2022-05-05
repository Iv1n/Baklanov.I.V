package FourthWork;

import Opis1.Opis1_1;

public class time extends Opis1_1 {

    private double storageTime;

    public time(long id, int productCode, String name, int wholesalePrice, int retailPrice, String description, double storageTime) {
        super(id, productCode, name, wholesalePrice, retailPrice, description);
        this.storageTime = storageTime;
    }

    public double getStorageTime() {
        return storageTime;
    }

    public void setStorageTime(double storageTime) {
        this.storageTime = storageTime;
    }

    public String toString() {
        return "\n" + super.toString() +
                "\n Максимальное время хранения (часы) - " + storageTime;
    }

}