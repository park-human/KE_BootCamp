
public class practice_0125 {
	public static void main(String[] args) {

		/*
		 * 2-14 int x = 1, y = 2;
		 * 
		 * System.out.println(x++); System.out.println(++x + y--);
		 * System.out.println(++x / 3 + x * ++y);
		 */

		/*
		 * 2-15 int x = 100;
		 * 
		 * System.out.println(x + "부터" + 200); System.out.println(x + 100 + "년 전");
		 * System.out.println("200" + "100" + " 어이쿠!");
		 */

		/*
		 * 2-16 int i1 = 0x11, i2 = 5; final int ONE = 1; char c1 = 'a'; float f1 =
		 * 1.5f; double d1 = 2.8; boolean b1 = true;
		 * 
		 * System.out.printf("i1 = %d\n", i2); System.out.printf("i1/2 = %d\n", i1 / 2);
		 * System.out.println("c1 + ONE = " + c1 + ONE);
		 * System.out.println("(int)c1 + ONE = " + (int) c1 + ONE);
		 * System.out.printf("(c1 + ONE) = %d\n", c1 + ONE);
		 * System.out.printf("(c1 + ONE) = %c\n", c1 + ONE);
		 * System.out.printf("(c1 + ONE) = %5s\n", c1 + ONE);
		 * System.out.printf("i2 + f1 = %f\n", i2 + f1);
		 * System.out.printf("f1 + d1 = %.1f\n", f1 + d1);
		 * System.out.printf("(int)(f1 + d1) = %d\n", (int) (f1 + d1));
		 * System.out.printf("(inf)f1 + (int)d1 = %d\n", (int) f1 + (int) d1);
		 * System.out.println("b1 = " + b1);
		 */

		/*
		 * a = 97; float f = 3.14f; int i = (int) f; System.out.println(i); int i = 100;
		 * char c = (char) i; System.out.println(c); int i = 1; boolean b = (boolean)i;
		 * System.out.println(b);
		 */

		// 연습문제 1
		// char a = 'a'; // A.
		// char b = "a"; // B. 문자는 '를 사용해야한다.
		// String c = "a"; // C. String
		// d = 'a'; // D. 문자열은 "를 사용해야한다.
		// char e='ab'; //E. 문자형은 한 문자를 표현하는 타입이다.
		// String f = "ab"; // F.

		// 연습문제 2
		// byte var1 = 128; // A.
		// byte는 -128~127 사이만 표현할 수 있다.
		// short var2 = 128; // B.
		// int var3 = 28L; // C.
		// int는 -231 ~ (231 - 1) 사이만 표현할 수 있다.
		// long var4 = 128L; // D.
		// float var5 = 123456.789123; // E. float는 7자리까지만 표현할 수 있다.
		// double var6 = 123456.789123; // F.

		// 연습문제 3
		byte var1 = 127;
		short var2 = 128;
		int var3 = 128;
		long var4 = 128L;
		var4 = var1;
		System.out.println(var1 + ", " + var2);
		var1 = (byte) var3;
		System.out.println(var1 + ", " + var3);

		float var5 = (float) 123456.789123;
		double var6 = 123456.789123;
		var5 = (float) var6;
		System.out.println(var5 + ", " + var6);
		var6 = var5;
		System.out.println(var5 + ", " + var6);

	}
}