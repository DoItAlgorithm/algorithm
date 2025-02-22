```java
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        char[] switches = br.readLine().toCharArray();
        char[] lamps = br.readLine().toCharArray();

        // boolean 배열로 변환
        boolean[] switchesA = new boolean[n];
        boolean[] switchesB = new boolean[n];
        boolean[] lampsC = new boolean[n];

        for(int i=0; i<n; i++){
            switchesA[i] = (switches[i]=='1');
            switchesB[i] = (switches[i]=='1');
            lampsC[i] = (lamps[i]=='1');
        }

        switchesB[0] = !switchesB[0];
        switchesB[1] = !switchesB[1];

        int cntA = 0;
        int cntB = 1;

        for(int i=1; i<n; i++){
            if(switchesA[i-1]!=lampsC[i-1]){
                switchesA[i] = !switchesA[i];
                if(i+1<n)
                    switchesA[i+1] = !switchesA[i+1];
                cntA++;
            }
            if(switchesB[i-1]!=lampsC[i-1]){
                switchesB[i] = !switchesB[i];
                if(i+1<n)
                    switchesB[i+1] = !switchesB[i+1];
                cntB++;
            }
        }

        if(switchesA[n-1]!=lampsC[n-1])
            cntA = Integer.MAX_VALUE;
        if(switchesB[n-1]!=lampsC[n-1])
            cntB = Integer.MAX_VALUE;

        int result = Math.min(cntA, cntB);
        if(result==Integer.MAX_VALUE)
            System.out.println(-1);
        else
            System.out.println(result);

    }
}
```