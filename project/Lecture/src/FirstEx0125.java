
public class FirstEx0125 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = 5;

		System.out.println("This is line new");
		System.out.print("Hello JAVA!\n");
		System.out.print("INHA\n");
		System.out.printf("decimal number = %d\n", 7);
		System.out.printf("a = %d\n", a, args);

		// float fv = 3.14f; 플로트 타입으로 변환하는 방법 1
		float fv = (float) 3.14; /* 플로트 타입으로 변환하는 방법 2 */
		double dv = 6.28;

		System.out.print("fv = " + fv + "\n");
		System.out.printf("fv = %f \n", fv);
		System.out.printf("fv = %.2f\n", fv);
		System.out.printf("fv = %07.2f\n", fv);
		System.out.printf("fv = %7.2f\n", fv);
		System.out.printf("fv = %-7.2f\n", fv);

		char ch = 'A';
		// char ch2 = "A"; // JAVA는 '와 "를 구별한다. ('는 문자character로, "는 문자열string으로 인식)
		System.out.printf("ch = %c\n", ch);
		// System.out.printf("ch = %c\n", ch2); ERROR!
		System.out.printf("ch = %d\n", (int) ch); // A의 아스키 코드를 10진수로 표현한 값

		String name = "gildong";
		System.out.printf("name = %s \n", name);
		System.out.println("name = " + name);
		System.out.print("name = " + name + "\n");

		final double PI = 3.14;
		// PI = 3.14 ; // 상수는 수정 불가..ERROR!
		System.out.printf("PI = %.2f\n", PI);

		byte b1 = 1;
		byte b2 = 2;
		// byte b3 = b1 + b2; → ERROR!

		int s = 15 / 2;
		int p = 13 % 4;
		System.out.printf("s = %d. p = %d\n", s, p);

		int m = 3;
		// m = m + 1;
		// ++m;
		// m++;
		// System.out.printf("m = %d\n, m");

	}

}