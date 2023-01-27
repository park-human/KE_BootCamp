package edu.gugudan;

public class GuGuDan {

	public static void main(String[] args) {
		int dan = 1, val = 2;

		for (dan = 1; dan <= 9; ++dan) {
			for (val = 2; val <= 9; ++val) {

				if (val == 6)
					break;

				System.out.printf("%d * %d = %d", val, dan, dan * val);
				System.out.print("\t");
			}
			System.out.print("\n");
		}
		System.out.print("\n");
		for (dan = 1; dan <= 9; ++dan) {
			for (val = 6; val <= 9; ++val) {

				System.out.printf("%d * %d = %d", val, dan, dan * val);
				System.out.print("\t");
			}
			System.out.print("\n");

		}
	}
}
