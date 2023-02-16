import java.io.*;
import java.net.*;
import java.util.*;

public class CalculatorServer {
    private Socket socket = null;

    public CalculatorServer(int port)
    {
        try {
            ServerSocket ss = new ServerSocket(port);
            Socket s = ss.accept();

            DataInputStream dis = new DataInputStream(s.getInputStream());
            DataOutputStream dos = new DataOutputStream(s.getOutputStream());

            while (true) {
                String input = dis.readUTF();
                if (input.equals("종료"))
                    break;
                System.out.println("방정식을 받았습니다.");
                int result = 0;

                StringTokenizer st = new StringTokenizer(input);
                int oprnd1 = Integer.parseInt(st.nextToken());
                String operation = st.nextToken();
                int oprnd2 = Integer.parseInt(st.nextToken());

                if (operation.equals("+")) {
                    result = oprnd1 + oprnd2;
                }
                else if (operation.equals("-")) {
                    result = oprnd1 - oprnd2;
                }
                else if (operation.equals("/")) {
                    result = oprnd1 / oprnd2;
                }
                else if (operation.equals("*")) {
                    result = oprnd1 * oprnd2;
                }
                System.out.println("결과를 보내는 중...");
                dos.writeUTF(Integer.toString(result));
            }
        }
        catch (Exception e) {
            System.out.println("오류 발생!");
        }
    }

    public static void main(String args[])
    {
        CalculatorServer server = new CalculatorServer(5000);
    }
}