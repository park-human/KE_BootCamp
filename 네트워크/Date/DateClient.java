package Date;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class DateClient {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("날짜 서버의 IP 주소는? ");
        String ipAddress = scanner.nextLine();
        try {
            Socket socket = new Socket(ipAddress, 9000);

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String date = in.readLine();
            System.out.println("현재 날짜와 시간: " + date);

            socket.close();
        } catch (UnknownHostException e) {
            System.err.println("호스트를 찾을 수 없음: " + e);
        } catch (IOException e) {
            System.err.println("예외 발생: " + e);
        }
    }
}
