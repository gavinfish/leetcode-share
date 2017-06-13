import java.util.Stack;

/**
 * Given an encoded string, return it's decoded string.
 * The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
 * You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
 * Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
 * <p>
 * Examples:
 * <p>
 * s = "3[a]2[bc]", return "aaabcbc".
 * s = "3[a2[c]]", return "accaccacc".
 * s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
 * <p>
 * Created by drfish on 6/13/2017.
 */
public class _394DecodeString {
    public String decodeString(String s) {
        Stack<Integer> countStack = new Stack<>();
        Stack<String> stringStack = new Stack<>();
        int index = 0;
        String curr = "";
        while (index < s.length()) {
            char c = s.charAt(index);
            if (Character.isDigit(c)) {
                int start = index;
                while (Character.isDigit(s.charAt(index + 1))) {
                    index++;
                }
                countStack.push(Integer.parseInt(s.substring(start, index + 1)));
            } else if (c == '[') {
                stringStack.push(curr);
                curr = "";
            } else if (c == ']') {
                StringBuilder sb = new StringBuilder(stringStack.pop());
                int repeatTimes = countStack.pop();
                for (int i = 0; i < repeatTimes; i++) {
                    sb.append(curr);
                }
                curr = sb.toString();
            } else {
                curr += c;
            }
            index++;
        }
        return curr;
    }

    public static void main(String[] args) {
        _394DecodeString solution = new _394DecodeString();
        assert "aaabcbc".equals(solution.decodeString("3[a]2[bc]"));
        assert "accaccacc".equals(solution.decodeString("3[a2[c]]"));
        assert "abcabccdcdcdef".equals(solution.decodeString("2[abc]3[cd]ef"));
    }
}
