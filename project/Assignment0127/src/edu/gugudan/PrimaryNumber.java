package edu.gugudan;

import java.util.Scanner;

public class PrimaryNumber {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		System.out.println("소수 구하기 프로그램");
		System.out.print("소수를 구할 정수 한 개 입력: ");
		int input = sc.nextInt();

		for (int i = 0; i <= input; i++) {
			isitprime(i);
		}
	}

	public static void isitprime(int number) {

		if (number < 2) {
			return;
		}
		if (number == 2) {
			System.out.printf("%d은(는) 소수이다.\n", number);
			return;
		}
		for (int i = 2; i < number; i++) {
			if (number % i == 0) {
				return;
			}
		}
		System.out.printf("%d은(는) 소수이다.\n", number);
		return;
	}
}