package edu.ifex;

import java.util.Scanner;

public class IfForEx0126 {

	public static void main(String[] args) {
		int a = 0;

		if (a > 0) {
			System.out.printf("a = %d는 양수이다. \n", a);
		} else if (a < 0) {
			System.out.printf("a = %d는 음수이다.\n", a);

		} else {
			System.out.printf("a는 0이다. \n");
		}

		// 학점 파별 문제
		Scanner sc = new Scanner(System.in);
		System.out.print("JAVA 점수(0~100) 입력 : ");
		int score = sc.nextInt();

		if (90 <= score && score <= 100) {
			System.out.printf("학점 : A (점수: %d점) \n", score);
		} else if (80 <= score && score <= 89) {
			System.out.printf("학점 : B (점수: %d점) \n", score);
		} else if (70 <= score && score <= 79) {
			System.out.printf("학점 : C (점수: %d점) \n", score);
		} else if (60 <= score && score <= 69) {
			System.out.printf("학점 : D (점수: %d점) \n", score);
		} else
			System.out.printf("학점 : F (점수: %d점) \n", score);

		//
		if (90 <= score) {
			System.out.printf("학점 : A (점수: %d점) \n", score);
		} else if (80 <= score) {
			System.out.printf("학점 : B (점수: %d점) \n", score);
		} else if (70 <= score) {
			System.out.printf("학점 : C (점수: %d점) \n", score);
		} else if (60 <= score) {
			System.out.printf("학점 : D (점수: %d점) \n", score);
		} else
			System.out.printf("학점 : F (점수: %d점) \n", score);

		int share = score / 10;
		if (share == 10 || share == 9)
			System.out.printf("학점 : A (점수: %d점) \n", score);
		else if (share == 8)
			System.out.printf("학점 : B (점수: %d점) \n", score);
		else if (share == 7)
			System.out.printf("학점 : C (점수: %d점) \n", score);
		else if (share == 6)
			System.out.printf("학점 : D (점수: %d점) \n", score);
		else
			System.out.printf("학점 : F (점수: %d점) \n", score);

	}

}
