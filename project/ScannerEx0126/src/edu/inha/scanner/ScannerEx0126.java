package edu.inha.scanner;

import java.util.Scanner;

//import java.util.Scanner;

public class ScannerEx0126 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int age = 0;
		char blood = '\0';
		double height = 0.0;
		String name = null; // String name = 0 ;

		System.out.print("나이를 입력하시오: ");
		age = sc.nextInt();
		System.out.printf("age = %d\n", age);

		sc.nextLine(); // 엔터(공백)문자를 처리하기 위함

		System.out.print("이름을 입력하시오: ");
		// name = sc.next(); 공백 포함 시 인식 못함
		name = sc.nextLine();
		System.out.printf("name = %s\n", name);

		System.out.print("혈액형을 입력하시오: ");
		blood = sc.next().charAt(0);
		System.out.printf("blood = %c\n", blood);

		System.out.print("신장을 입력하시오: ");
		height = sc.nextDouble();
		System.out.printf("height = %.2fcm \n", height);

	}

}
