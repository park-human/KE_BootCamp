package edu.switchtwo;

public class SwitchEx2 {

	public static void main(String[] args) {
		whoIsIt("호랑이");
		whoIsIt("사자");
		whoIsIt("독수리");
		whoIsIt("참새");
		whoIsIt("고등어");
		whoIsIt("곰팡이");
	} // end of main()

	static void whoIsIt(String bio) {
		String kind = "";
		switch (bio) {
		case "호랑이":
		case "사자":
			kind = "포유류";
			break;
		case "독수리":
		case "참새":
			kind = "조류";
			break;
		case "고등어":
			kind = "어류";
			break;
		default:
			System.out.print("어이쿠! ");
			kind = "...";
		} // end of switch()

		System.out.printf("%s는 %s이다.\n", bio, kind);

	}

}