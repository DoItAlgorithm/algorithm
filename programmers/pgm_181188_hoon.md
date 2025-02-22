```java
import java.util.*;
class Solution {


    public int solution(int[][] targets) {
        
        Arrays.sort(targets, (o1, o2)-> o1[1]-o2[1]);
        int std = 0;
        int cnt = 0;
        
        for(int i=0, len=targets.length; i<len; i++){
            if(targets[i][0]>=std){
                std = targets[i][1];
                cnt++;
            }
        }
        
        return cnt;
    }
}
```