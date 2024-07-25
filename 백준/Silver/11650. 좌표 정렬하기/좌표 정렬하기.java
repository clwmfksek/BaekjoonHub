import java.util.*;

// 점을 표현하는 클래스(Point)에 대한 Comparable<Point> 인터페이스 구현
class Point implements Comparable<Point> {
    int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    // compareTo 메서드 선언
    public int compareTo(Point other) {
        // x 좌표가 다르면 x 좌표를 기준으로 비교
        if (this.x != other.x) {
            return Integer.compare(this.x, other.x);
        } else { // x 좌표가 같으면 y 좌표를 기준으로 비교
            return Integer.compare(this.y, other.y);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 점의 개수 N 입력
        int N = scanner.nextInt();
        List<Point> points = new ArrayList<>();

        // N개의 점을 저장
        for (int i = 0; i < N; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            // 입력받은 좌표로 Point 객체를 생성하여 리스트에 추가
            points.add(new Point(x, y));
        }

        // 정렬 후 출력
        Collections.sort(points); // 정렬을 위해 Collections.sort 메서드 사용
        for (Point point : points) {
            // 정렬된 점들을 순서대로 출력
            System.out.println(point.x + " " + point.y);
        }
    }
}
