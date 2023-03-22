public class Car {
    // Class example, initial attribute
    int speed;


    public Car(/*constructor arguments can be input here */){
        // Constructor example, sets attribute
        speed = 10;
    }
    public void speedUp(int x){
        // Public method, requires obj construction to call
        speed += x;
        System.out.println("speed is now " + speed);

    }
    static void staticMethod(){
        // Static method, does not require object constructions
        System.out.println("Test");
    }

// No main compiler method because it will be called in test file

}
