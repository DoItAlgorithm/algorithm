```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static int[] arr;
    public static boolean[] visited;
    public static int[] tem;
    public static Set<String> set;

    public static void combination(int m, int cnt){
        if(cnt==m){
            StringBuilder sb = new StringBuilder();
            for(int a : tem)
                sb.append(a).append(" ");
            if(!set.contains(sb.toString())){
                set.add(sb.toString());
                System.out.println(sb.toString());
            }
            return;
        }
        for(int i=0, len=arr.length; i<len; i++){
            if(!visited[i]){
                visited[i] = true;
                tem[cnt] = arr[i];
                combination(m, cnt+1);
                visited[i] = false;
            }
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        arr = new int[n];
        tem = new int[m];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        visited = new boolean[n];
        set = new HashSet<>();
        combination(m, 0);

    }
}
```