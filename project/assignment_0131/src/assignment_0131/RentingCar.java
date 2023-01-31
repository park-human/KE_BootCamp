package assignment_0131;

import java.util.Scanner;

class Car {
  protected int speed, carNumber;
  protected String carName, carColor, driverAddress;

  public Car(int speed, int carNumber, String carName, String carColor, String driverAddress) {
    this.speed = speed;
    this.carNumber = carNumber;
    this.carName = carName;
    this.carColor = carColor;
    this.driverAddress = driverAddress;
  }

  public void increaseSpeed(int increase) {
    speed += increase;
  }

  public void decreaseSpeed(int decrease) {
    speed -= decrease;
  }
}

class LentCar extends Car {
  private int fare;
  private String comp;

  public LentCar(int speed, int carNumber, String carName, String carColor, String driverAddress, int fare, String comp) {
    super(speed, carNumber, carName, carColor, driverAddress);
    this.fare = fare;
    this.comp = comp;
  }

  public int getFare() {
    return fare;
  }

  public String getComp() {
    return comp;
  }
}


public class RentingCar {

	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    
	    
	    System.out.print("자동차 종류를 입력하시오. : ");
        String carName = sc.nextLine();
	    System.out.print("자동차 색깔을 입력하시오. : ");
        String carColor = sc.nextLine();
	    System.out.print("자동차 번호를 입력하시오. : ");
        int carNumber = sc.nextInt();
        sc.nextLine();
        System.out.print("운전자 주소를 입력하시오. : ");
        String driverAddress = sc.nextLine();
        System.out.print("자동차 속도를 입력하시오. : ");
        int speed = sc.nextInt();
        sc.nextLine();
        System.out.print("렌트비를 입력하시오. : ");
        int getFare = sc.nextInt();
        sc.nextLine();
        System.out.print("렌트 회사를 입력하시오. : ");
        String getComp = sc.nextLine();
	    
        LentCar car = new LentCar(speed, carNumber, carName, carColor, driverAddress, getFare, getComp);
	    System.out.println("자동차 종류: " + car.carName);
	    System.out.println("자동차 색깔: " + car.carColor);
	    System.out.println("자동차 번호: " + car.carNumber);
	    System.out.println("운전자 주소: " + car.driverAddress);
	    System.out.println("현재 자동차의 속도는 시속 " + car.speed + "km/h입니다.");
	    System.out.println("렌트 요금: " + car.getFare());
	    System.out.println("렌트 회사명: " + car.getComp());
	    System.out.print("속도를 얼마나 올리시겠습니까? : ");
	    int increase = sc.nextInt();
	    car.increaseSpeed(increase);
	    System.out.println("현재 자동차의 속도는 시속 : " + car.speed + "km/h 입니다.");
	    System.out.print("속도를 얼마나 내리시겠습니까? : ");
	    int decrease = sc.nextInt();
	    car.decreaseSpeed(decrease);
	    System.out.println("현재 자동차의 속도는 시속 : " + car.speed + "km/h 입니다.");
	  }
	}