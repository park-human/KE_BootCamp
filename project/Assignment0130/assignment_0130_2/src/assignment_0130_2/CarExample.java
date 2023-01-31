package assignment_0130_2;

public class CarExample {
	public static void main(String[] args) {
		// Car 객체 생성
		Car myCar = new Car();
		
		// Car 객체의 필드값 읽기
		System.out.println("차 이름 : " + myCar.name);
		System.out.println("차 색 : " + myCar.color);
		System.out.println("차량 번호 : " + myCar.number);
		System.out.println("운전자 주소 : " + myCar.address);
		System.out.println("속도 : " + myCar.speed);
		
	}
}