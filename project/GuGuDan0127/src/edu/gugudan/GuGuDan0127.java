package edu.gugudan;

public class GuGuDan0127 {

	public static void main(String[] args) { // 이중 for
		int dan = 2, val = 1;

		for (dan = 2; dan <= 9; ++dan) {
			for (val = 1; val <= 9; ++val) {

				// 각 단에서 value = 4의 경우만 출력하지 않기 - continue
				// if (val == 4)
				// continue;

				// 각 단에서 value가 3일때까지만 출력 - break
				if (val == 4)
					break;

				System.out.printf("%d * %d = %d", dan, val, dan * val);
				System.out.print("\t");
			}
			System.out.print("\n");
		}

		for (int i = 1; i <= 10; ++i) {
			if (i == 4)
				continue;
			System.out.printf("나 실행될까?");

			// if (i == 6)
			// break;
			System.out.printf("i = %d\t", i);
		}
	}

}
