import java.util.List;

public class Day23Assignment {
    public static void main(String[] args){
        List<String> names = List.of("홍길동", "배정화", "임꺽정", "연흥부", "김선달", "황진이");

        List<String> filterednames = names.stream()
                .filter(name -> name.compareTo("이") < 0)
                .toList();
        System.out.println("②의 결과: " + filterednames);

        List<String> sortednames = names.stream()
                .sorted()
                .toList();
        System.out.println("③의 결과 : " + sortednames);

        System.out.println("④의 결과 : " + names.stream().findFirst());
        String firstElement = names.stream()
                .findFirst()
                .orElseThrow();
        System.out.println(firstElement);

        System.out.println("⑤의 결과 : " + names.size());

    }
}
