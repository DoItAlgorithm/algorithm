```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static class Jewel {
        int weight;
        int price;

        public Jewel(int weight, int price){
            this.weight = weight;
            this.price = price;
        }
    }

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Jewel[] jewels = new Jewel[n];
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            jewels[i] = new Jewel(m, v);
        }

        // 보석들을 무게 오름차순으로 정렬
        Arrays.sort(jewels, new Comparator<Jewel>(){
            @Override
            public int compare(Jewel o1, Jewel o2){
                return o1.weight-o2.weight;
            }
        });

        // 가방의 무게를 오름차순으로 정렬
        List<Integer> bags = new ArrayList<>();
        for(int i=0; i<k; i++){
            int c = Integer.parseInt(br.readLine());
            bags.add(c);
        }
        Collections.sort(bags);

        // 우선순위큐는 가격이 내림차순으로 정렬
        PriorityQueue<Jewel> pq = new PriorityQueue<>(new Comparator<Jewel>() {
            @Override
            public int compare(Jewel o1, Jewel o2) {
                return o2.price-o1.price;
            }
        });

        int idx = 0;
        long total = 0;
        for(int i=0, len=bags.size(); i<len; i++){
            int c = bags.get(i);
            // 현재 가방의 무게보다 작은 보석들을 모두 pq에 삽입
            while (idx<n && jewels[idx].weight<=c){
                pq.offer(jewels[idx]);
                idx++;
            }
            // pq에서 가격이 제일 비싼 보석 추출
            if(!pq.isEmpty())
                total += pq.poll().price;
        }
        System.out.println(total);
    }
}
```