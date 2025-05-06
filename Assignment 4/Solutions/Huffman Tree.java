import java.util.*;
import java.util.Map;

class HuffmanNode implements Comparable<HuffmanNode> {
    int freq;
    Character character;
    HuffmanNode left;
    HuffmanNode right;

    public HuffmanNode(int freq, Character character, HuffmanNode left, HuffmanNode right) {
        this.freq = freq;
        this.character = character;
        this.left = left;
        this.right = right;
    }

    @Override
    public int compareTo(HuffmanNode other) {
        return this.freq - other.freq;
    }
}

public class Main {
    private static Map<Character, String> codeDict = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        // Frequency for distinct chars
        Map<Character, Integer> freqDict = new HashMap<>();
        for (char c : input.toCharArray()) {
            freqDict.put(c, freqDict.getOrDefault(c, 0) + 1);
        }

        if (freqDict.size() == 1) {
            System.out.println(input.length());
            return;
        }

        // Construct Huffman tree
        PriorityQueue<HuffmanNode> freqHeap = new PriorityQueue<>();
        for (Map.Entry<Character, Integer> entry : freqDict.entrySet()) {
            freqHeap.add(new HuffmanNode(entry.getValue(), entry.getKey(), null, null));
        }

        while (freqHeap.size() != 1) {
            HuffmanNode left = freqHeap.poll();
            HuffmanNode right = freqHeap.poll();
            HuffmanNode node = new HuffmanNode(left.freq + right.freq, null, left, right);
            freqHeap.add(node);
        }

        // Construct codes
        HuffmanNode root = freqHeap.peek();
        createCode(root, "");

        // Calculate total bits
        int bits = 0;
        for (char c : input.toCharArray()) {
            bits += codeDict.get(c).length();
        }
        System.out.println(bits);
    }

    private static void createCode(HuffmanNode start, String curCode) {
        if (start != null && start.character != null) {
            codeDict.put(start.character, curCode);
        } else if (start != null) {
            createCode(start.left, curCode + "0");
            createCode(start.right, curCode + "1");
        }
    }
}