public class Test{

    static void myMethod(){
        System.out.println("Test");
    }











    
    
    
    public static void main(String[] args){
        System.out.println("Hello World");
        String x="1";
        String y="2";
        double randomNum = Math.random();
        System.out.println(randomNum);
        myMethod();

        Car ferrari = new Car();
        System.out.println(ferrari.speed);
        ferrari.speedUp(5);
        Car.staticMethod();
        
    }
}