// StringBuilder vs String
// string append
public class Test {
    public static void main(String[] args){
        String s = new String("hi");
        long start = System.nanoTime();
        for (int i = 1; i<1000 ; i++)
            s = s + "!";
        long end = System.nanoTime();
        System.out.println(end - start);

        StringBuilder sb = new StringBuilder("hi");
        start = System.nanoTime();
        for (int i = 1; i < 1000 ; i++)
            sb = sb.append("!");
        end = System.nanoTime();
        System.out.println(end - start);
    }
}
