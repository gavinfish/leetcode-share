import java.util.Stack;

/**
 * Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
 * <p>
 * Example:
 * Given "bcabc"
 * Return "abc"
 * <p>
 * Given "cbacdcbc"
 * Return "acdb"
 * <p>
 * Credits:
 * Special thanks to @dietpepsi for adding this problem and creating all test cases.
 * <p>
 * Created by drfish on 6/8/2017.
 */
public class _316RemoveDuplicateLetters {
    public String removeDuplicateLetters(String s) {
        if (s == null) {
            return null;
        }
        int[] count = new int[26];
        boolean[] visited = new boolean[26];
        char[] chars = s.toCharArray();
        for (char c : chars) {
            count[c - 'a']++;
        }
        Stack<Character> stack = new Stack<>();
        int index;
        for (char c : chars) {
            index = c - 'a';
            count[index]--;
            if (visited[index]) {
                continue;
            }
            while (!stack.isEmpty() && c < stack.peek() && count[stack.peek() - 'a'] != 0) {
                visited[stack.pop() - 'a'] = false;
            }
            stack.push(c);
            visited[index] = true;
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.insert(0, stack.pop());
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        _316RemoveDuplicateLetters solution = new _316RemoveDuplicateLetters();
        assert "abc".equals(solution.removeDuplicateLetters("bcabc"));
        assert "acdb".equals(solution.removeDuplicateLetters("cbacdcbc"));
    }
}
