
public class OperateEx {

	public static void main(String[] args) {
		int a = 1;
		System.out.printf("a = %d\n", a);
		a = a + 1;
		System.out.printf("a+1 = %d\n", a);
		++a; // a = a + 1;와 같은 역할
		System.out.printf("++a 후 a = %d\n", a);
		a++;
		System.out.printf("a++ 후 a = %d\n", a);
		// 여기까지 실행 후 a = 4
		System.out.printf("++a 후 a = %d\n", ++a);
		System.out.printf("a++ 후 a = %d\n", a++);
		System.out.printf("최종 a = %d\n", a);

		int b = 9;
		System.out.printf("b = %d\n", b);
		b = b - 1;
		System.out.printf("b-1 = %d\n", b);

		--b; // b = b-1 ;와 같은 역할
		System.out.printf("--b한 후 b = %d\n", b);
		b--;
		System.out.printf("b--한 후 b = %d\n", b);

		int c = 8, d = 7;
		int max = (c > d) ? c : d; // ? - 조건연산자
		System.out.printf("max = d%\n, max");
	}

}
