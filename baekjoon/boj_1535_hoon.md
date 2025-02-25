```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] staminaArr = new int[n+1];
        int[] delightArr = new int[n+1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            staminaArr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            delightArr[i] = Integer.parseInt(st.nextToken());
        }

        final int initialStamina = 100;
        int[] dp = new int[initialStamina];

        // dp 수행
        for(int i=0; i<n; i++){
            int stamina = staminaArr[i];
            int delight = delightArr[i];
            for(int j=initialStamina-1; j>=stamina; j--){
                dp[j] = Math.max(dp[j], dp[j-stamina]+delight);
            }
        }

        // 최대 기쁨 출력
        int answer = 0;
        for(int i=0; i<initialStamina; i++){
            answer = Math.max(answer, dp[i]);
        }

        System.out.println(answer);
    }
}

```