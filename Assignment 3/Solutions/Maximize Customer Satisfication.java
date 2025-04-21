import java.io.*;
import java.util.*;

public class Main {
    static class Product {
        int p;
        int r;
        int sum;
        
        Product(int p, int r, int sum) {
            this.p = p;
            this.r = r;
            this.sum = sum;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        int[] perf = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            perf[i] = Integer.parseInt(st.nextToken());
        }
        
        int[] reli = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            reli[i] = Integer.parseInt(st.nextToken());
        }
        
        int[][] requests = new int[m][2];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            requests[i][0] = Integer.parseInt(st.nextToken());
            requests[i][1] = Integer.parseInt(st.nextToken());
        }
        
        List<Product> products = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            products.add(new Product(perf[i], reli[i], perf[i] + reli[i]));
        }
        
        products = heapSort(products);
        
        for (int[] request : requests) {
            int min_p = request[0];
            int min_r = request[1];
            boolean found = false;
            
            for (Product product : products) {
                if (product.p >= min_p && product.r >= min_r) {
                    bw.write(product.sum + " ");
                    found = true;
                    break;
                }
            }
            
            if (!found) {
                bw.write("-1 ");
            }
        }
        bw.flush();
    }
    
    private static List<Product> heapSort(List<Product> unsorted) {
        PriorityQueue<Product> maxHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(b.sum, a.sum)
        );
        maxHeap.addAll(unsorted);
        List<Product> sorted = new ArrayList<>();
        while (!maxHeap.isEmpty()) {
            sorted.add(maxHeap.poll());
        }
        return sorted;
    }
}
