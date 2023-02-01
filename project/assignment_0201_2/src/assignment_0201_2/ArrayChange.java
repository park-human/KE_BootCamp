package assignment_0201_2;

import java.util.Arrays;

public class ArrayChange {
	public static void main(String[] args) {
		int[] num = new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
		for (int i = 0; i < num.length / 2 ; i++) {
			int temp = num[i * 2];
			num[i * 2] = num[i * 2 + 1];
			num[i * 2 + 1] = temp;
		}
		System.out.println(Arrays.toString(num));
	}
}
