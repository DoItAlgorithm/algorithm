```java
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static boolean flag = false;

    public static void dfs(String s, String t){

        if(s.length()>=t.length()){
            if(s.toString().equals(t)){
                flag = true;
            }
            return;
        }

        if(t.endsWith("A")){
            dfs(s, t.substring(0, t.length()-1));
        }

        if(t.startsWith("B")){
            StringBuilder sb = new StringBuilder(t);
            sb.deleteCharAt(0).reverse();
            dfs(s, sb.toString());
        }
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        String t = br.readLine();
        dfs(s, t);

        System.out.println(flag==true ? 1:0);
    }
}

```