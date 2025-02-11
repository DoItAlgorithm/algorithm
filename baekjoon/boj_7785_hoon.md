```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

import static java.util.Collections.reverseOrder;

public class Main {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashSet<String> set = new HashSet<>();
        for(int i=0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String command = st.nextToken();
            if(command.equals("enter")){
                set.add(name);
            }
            else{
                set.remove(name);
            }
        }

        List<String> list = new ArrayList<>(set);

        Collections.sort(list, reverseOrder());
        for(String name : list){
            System.out.println(name);
        }
    }
}
```