class One{
    public One(){
    }
    public static One produceOneInstance(){
        return new One();
    }
}

public class Test{
    public static void main(String[] args){
        // One o = new One
        One o1 = One.produceOneInstance();
        One o2 = One.produceOneInstance();
    }
}

//import java.net.*;
//
//// StringBuilder vs String
//// string append
//
//public class Test{
//    public static String getMACIdentifier(NetworkInterface network) {
//        StringBuilder identifier = new StringBuilder();
//        try {
//            byte[] macBuffer = network.getHardwareAddress();
//            if (macBuffer != null) {
//                for (int i = 0; i < macBuffer.length; i++) {
//                    identifier.append(
//                            String.format("%02X%s",macBuffer[i],
//                                    (i < macBuffer.length - 1)
//                                            ? "-" : ""));
//                }
//            } else {
//                return "---";
//            }
//        } catch (SocketException ex) {
//            ex.printStackTrace();
//        }
//        return identifier.toString(); // 스트링빌더 객체를 문자열로 변환 후 리턴
//    }
//    public static void main(String[] args) throws UnknownHostException, SocketException {
//        InetAddress addr = InetAddress.getLocalHost();
//        System.out.println("IP 주소 : " + addr.getHostAddress());
//        NetworkInterface network = NetworkInterface.getByInetAddress(addr);
//        System.out.println("MAC 주소 : " + getMACIdentifier(network));
//    }
//}
