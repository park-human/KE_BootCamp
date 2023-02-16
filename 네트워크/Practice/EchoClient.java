package Practice;

import java.io.*;
import java.net.*;
import java.util.*;

public class EchoClient {
    public static void main(String[] args) throws IOException {
        Socket client = null;
        PrintWriter out = null;

        try{
            client = new Socket();
            System.out.println("에코 서버와 연결 시도...");
            client.connect(new InetSocketAddress("localhost", 5000), 3000);
            System.out.println("에코 서버와 연결 성공");
        } catch (Exception e){
        }

        out = new PrintWriter(client.getOutputStream(), true);

        Scanner in = new Scanner(System.in);
        String msg;

        System.out.print("보낼 메시지를 입력하세요 : ");
        while ((msg = in.nextLine()) != null){
            if (msg.contains("끝"))
                break;
            out.println(msg);
            System.out.println("보낼 메시지를 입력하세요 : ");
        }

        System.out.print("클라이언트 종료");
        out.close();
        in.close();
        client.close();
    }
}
