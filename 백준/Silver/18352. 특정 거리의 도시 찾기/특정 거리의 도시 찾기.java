import java.util.*;
import java.io.*;

public class Main {

    // BFS 함수: 주어진 시작 노드에서 BFS를 수행하여 최단 거리를 계산합니다.
    public static void bfs(int start, ArrayList<ArrayList<Integer>> graph, int[] distance){
        Deque<Integer> deque = new ArrayDeque<>();
        deque.add(start);
        distance[start] = 0;
        while(!deque.isEmpty()){  // 오류 수정: isEmpty()가 아니라 !isEmpty()로 변경
            int now = deque.poll();
            for(int i=0; i<graph.get(now).size(); i++){
                int next = graph.get(now).get(i);
                if(distance[next] == -1){
                    distance[next] = distance[now] + 1;
                    deque.add(next);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());  // 노드 수
        int m = Integer.parseInt(st.nextToken());  // 간선 수
        int k = Integer.parseInt(st.nextToken());  // 목표 거리
        int x = Integer.parseInt(st.nextToken());  // 시작 노드

        int[] distance = new int[n+1];
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i=0; i<=n; i++){
            graph.add(new ArrayList<Integer>());
            distance[i] = -1;  // 모든 거리를 -1로 초기화 (방문하지 않음을 의미)
        }

        // 간선 정보 입력 받아 그래프 구성
        for(int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
        }

        // BFS 실행
        bfs(x, graph, distance);

        // 결과를 저장할 리스트
        ArrayList<Integer> result = new ArrayList<>();
        for(int i=1; i<=n; i++){
            if(distance[i] == k){
                result.add(i);
            }
        }

        // 결과 출력
        if(result.isEmpty()) {
            System.out.println(-1);
        } else {
            for(int i=0; i<result.size(); i++){
                System.out.println(result.get(i));
            }
        }
    }
}
