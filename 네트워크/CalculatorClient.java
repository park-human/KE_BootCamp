import java.io.*;
import java.net.*;
import java.util.*;

public class CalculatorClient {
    private Socket s = null;
    public CalculatorClient(String address, int port)
    {
        try {
            Scanner sc = new Scanner(System.in);
            s = new Socket(address, port);
            System.out.println("연결 완료");

            DataInputStream dis = new DataInputStream(s.getInputStream());
            DataOutputStream dos = new DataOutputStream(s.getOutputStream());

            while (true) {
                System.out.println("피연산자 형식으로 연산을 입력하세요");
                System.out.println("예) 3 + 5 ");
                String inp = sc.nextLine();

                if (inp.equals("종료"))
                    break;
                dos.writeUTF(inp);

                String ans = dis.readUTF();
                System.out.println("답 = " + ans);
            }
        }
        catch (Exception e) {
            System.out.println("연결 오류 발생!");
        }
    }

    public static void main(String args[])
    {
        CalculatorClient client = new CalculatorClient("127.0.0.1", 5000);
    }
}