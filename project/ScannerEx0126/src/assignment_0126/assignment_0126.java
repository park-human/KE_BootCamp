package assignment_0126;

import java.util.Scanner; // Scanner 클래스 호출

public class assignment_0126 {

	public static void main(String[] args) {

		// 2일차 1번 문제

		Scanner sc = new Scanner(System.in); // Scanner 객체 생성

		String name, major, address = null;
		int eng, phy, cal = 0;

		System.out.print("이름을 입력하세요 \n");
		name = sc.nextLine();

		System.out.print("학과명을 입력하세요 \n");
		major = sc.nextLine();

		System.out.print("영어 점수 입력: ");
		eng = sc.nextInt();
		System.out.print("물리학 점수 입력: ");
		phy = sc.nextInt();
		System.out.print("미적분학 점수 입력: ");
		cal = sc.nextInt();

		sc.nextLine();

		System.out.print("주소를 입력하세요 \n");
		address = sc.nextLine();

		System.out.printf("이름 = %s, ", name);
		System.out.printf("학과명 = %s \n", major);
		System.out.printf("영어 = %d, ", eng);
		System.out.printf("물리학 = %d, ", phy);
		System.out.printf("미적분학 = %d \n", cal);
		System.out.printf("주소 = %s", address);

		// 2일차 2번 문제
	}

}
