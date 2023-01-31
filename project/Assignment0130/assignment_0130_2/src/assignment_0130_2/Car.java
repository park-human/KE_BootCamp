package assignment_0130_2;

import java.util.Scanner;

public class Car {
	String name, color, address;
	int number, speed;
}

class input {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("차 이름을 입력하시오.");
		name = sc.next();
		System.out.println("차 색을 입력하시오.");
		age = sc.nextInt();
		System.out.println("차량 번호를 입력하시오.");
		height = sc.nextDouble();
		System.out.println("운전자 주소를 입력하시오.");
		buffer = sc.nextLine();
		System.out.println("속도를 입력하시오.");
		intro = sc.nextLine();
		
		System.out.println("이름은 "+name+"나이는 "+age+",키는 "+height+"입니다.");
		System.out.println(intro);
	}
}
