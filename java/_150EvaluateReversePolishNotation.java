import java.util.Stack;

/**
 * Evaluate the value of an arithmetic expression in Reverse Polish Notation.
 * Valid operators are +, -, *, /. Each operand may be an integer or another expression.
 * <p>
 * Some examples:
 * ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 * ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
 * <p>
 * Created by drfish on 6/8/2017.
 */
public class _150EvaluateReversePolishNotation {
    public int evalRPN(String[] tokens) {
        if (tokens == null) {
            return 0;
        }
        Stack<Integer> stack = new Stack<>();
        for (String token : tokens) {
            switch (token) {
                case "+":
                    stack.push(stack.pop() + stack.pop());
                    break;
                case "*":
                    stack.push(stack.pop() * stack.pop());
                    break;
                case "-":
                    int second = stack.pop();
                    int first = stack.pop();
                    stack.push(first - second);
                    break;
                case "/":
                    second = stack.pop();
                    first = stack.pop();
                    stack.push(first / second);
                    break;
                default:
                    stack.push(Integer.valueOf(token));
            }
        }
        return stack.pop();
    }

    public static void main(String[] args) {
        _150EvaluateReversePolishNotation solution = new _150EvaluateReversePolishNotation();
        assert 9 == solution.evalRPN(new String[]{"2", "1", "+", "3", "*"});
        assert 6 == solution.evalRPN(new String[]{"4", "13", "5", "/", "+"});
    }
}
