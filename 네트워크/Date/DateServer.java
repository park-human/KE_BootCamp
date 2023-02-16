package Date;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

public class DateServer {
    public static void main(String[] args) {
            try {
                ServerSocket serverSocket = new ServerSocket(9000);
                System.out.println("서버 시작");

                while (true) {
                    Socket clientSocket = serverSocket.accept();

                    PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
                    out.println(new Date().toString());

                    clientSocket.close();
                }
            } catch (IOException e) {
                System.err.println("예외 발생: " + e);
                }
    }
}