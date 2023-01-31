package assignment_0130;

import java.util.Scanner;

public class LotteryProgram {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] num = new int[6];
		
		for(int i=0; i < num.length; i++){
		System.out.print("로또번호 입력 : ");
		num[i] = sc.nextInt();
	    
		// 중복 검사
		for (int j = 0; j < i; j++)
			if (num[i] == num[j]) {
                i--;
				System.out.println("같은 번호가 있습니다!");
				break;
			}
		}
		
		System.out.print("입력된 로또 번호 : ");
			for(int i=0; i < num.length; i++) {
				System.out.print(num[i]+" ");
	}
			System.out.println("");
			System.out.printf("계속하려면 아무 키나 누르십시오");
}
}