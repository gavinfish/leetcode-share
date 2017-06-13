import java.util.Stack;

/**
 * Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
 * <p>
 * Note:
 * The length of num is less than 10002 and will be ≥ k.
 * The given num does not contain any leading zero.
 * <p>
 * Example 1:
 * Input: num = "1432219", k = 3
 * Output: "1219"
 * Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
 * <p>
 * Example 2:
 * Input: num = "10200", k = 1
 * Output: "200"
 * Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
 * <p>
 * Example 3:
 * Input: num = "10", k = 2
 * Output: "0"
 * Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 * <p>
 * Created by drfish on 6/13/2017.
 */
public class _402RemoveKDigits {
    public String removeKdigits(String num, int k) {
        if (num.length() <= k) {
            return "0";
        }
        Stack<Character> stack = new Stack<>();
        int index = 0;
        // remove digit which is bigger than its next one
        while (index < num.length()) {
            while (k > 0 && !stack.isEmpty() && stack.peek() > num.charAt(index)) {
                stack.pop();
                k--;
            }
            stack.push(num.charAt(index));
            index++;
        }
        while (k > 0) {
            stack.pop();
            k--;
        }
        // construct new number
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        sb.reverse();
        // remove zeros at the head
        while (sb.length() > 1 && sb.charAt(0) == '0') {
            sb.deleteCharAt(0);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        _402RemoveKDigits solution = new _402RemoveKDigits();
        assert "1219".equals(solution.removeKdigits("1432219", 3));
        assert "200".equals(solution.removeKdigits("10200", 1));
        assert "0".equals(solution.removeKdigits("10", 2));
    }
}
