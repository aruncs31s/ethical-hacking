import java.net.*;
import java.io.*;

public class WebServer {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(8080);

while (true) {
 Socket clientSocket = serverSocket.accept();

 BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
String inputLine;
 while ((inputLine = in.readLine()) != null) {
  System.out.println(inputLine);
  if (inputLine.isEmpty()) {
                    break;
                }
            }
            
 PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
            out.println("HTTP/1.1 200 OK");
            out.println("Content-Type: text/html");
            out.println();
            out.println("<html><body>Hello, World!</body></html>");

            clientSocket.close();
        }
    }
}
