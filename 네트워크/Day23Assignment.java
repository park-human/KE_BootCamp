import java.util.List;
import java.util.OptionalDouble;
import java.util.stream.Stream;

enum Gender {남, 여}
public class Day23Assignment {
    public static void main(String[] args){

        List<String> names = List.of("홍길동", "배정화", "임꺽정", "연흥부", "김선달", "황진이");
        List<Integer> ages = List.of(25, 20, 29, 28, 32, 18);
        List<Gender> genders = List.of(Gender.남, Gender.여, Gender.남, Gender.남, Gender.남, Gender.여);

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

        int sumOfAges = ages.stream().reduce(0, Integer::sum);
        System.out.println(sumOfAges);
        int maxAge = ages.stream().reduce(0, Integer::max);
        System.out.println(maxAge);
        OptionalDouble averageAge = ages.stream().mapToInt(Integer::intValue).average();
        System.out.println(averageAge.getAsDouble());

    }
}

class Member {
    String name;
    Gender gender;
    int age;
    static void main(String[] args) {
        List<String> names = List.of("홍길동", "배정화", "임꺽정", "연흥부", "김선달", "황진이");
        List<Integer> ages = List.of(25, 20, 29, 28, 32, 18);
        List<Gender> genders = List.of(Gender.남, Gender.여, Gender.남, Gender.남, Gender.남, Gender.여);
        int index = 0; // 정적 정수 필드

        Stream<Member> memberStream = names.stream()
                .map(name -> new Member(name, genders.get(index), ages.get(index++)));

        memberStream.forEach(System.out::println);
    }
}
