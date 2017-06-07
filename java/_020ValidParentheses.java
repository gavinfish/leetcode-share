import java.util.Stack;

/**
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 * The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
 * <p>
 * Created by drfish on 6/7/2017.
 */
public class _020ValidParentheses {
    public boolean isValid(String s) {
        if (s == null) {
            return true;
        }
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            switch (c) {
                case '(':
                    stack.push(')');
                    break;
                case '{':
                    stack.push('}');
                    break;
                case '[':
                    stack.push(']');
                    break;
                default:
                    if (stack.isEmpty() || stack.pop() != c) {
                        return false;
                    }
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        _020ValidParentheses solution = new _020ValidParentheses();
        assert solution.isValid("()");
        assert solution.isValid("()[]()");
        assert !solution.isValid("(]");
        assert !solution.isValid("([)]");
    }
}
