package edu.forexone;

public class ForExOne0127 {

	public static void main(String[] args) {
		int i = 0, sum = 0;

		for (i = 0; i <= 10; ++i) {
			// sum = sum + i;
			sum += i;
			if (i % 2 == 0)
				System.out.printf("i = %d\t", i);
		}

		System.out.printf("sum = %d, i = %d\n", sum, i);
	}

}
