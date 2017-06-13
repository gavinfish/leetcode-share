import java.util.List;
import java.util.Stack;

/**
 * Given a nested list of integers represented as a string, implement a parser to deserialize it.
 * Each element is either an integer, or a list -- whose elements may also be integers or other lists.
 * <p>
 * Note: You may assume that the string is well-formed:
 * String is non-empty.
 * String does not contain white spaces.
 * String contains only digits 0-9, [, - ,, ].
 * <p>
 * Example 1:
 * Given s = "324",
 * You should return a NestedInteger object which contains a single integer 324.
 * <p>
 * Example 2:
 * Given s = "[123,[456,[789]]]",
 * Return a NestedInteger object containing a nested list with 2 elements:
 * <p>
 * 1. An integer containing value 123.
 * 2. A nested list containing two elements:
 * i.  An integer containing value 456.
 * ii. A nested list with one element:
 * a. An integer containing value 789.
 * <p>
 * Created by drfish on 6/9/2017.
 */
public class _385MiniParser {
    /**
     * // This is the interface that allows for creating nested lists.
     * // You should not implement it, or speculate about its implementation
     **/
    public interface INestedInteger {
//          // Constructor initializes an empty nested list.
//          public NestedInteger();
//
//          // Constructor initializes a single integer.
//          public NestedInteger(int value);

        // @return true if this NestedInteger holds a single integer, rather than a nested list.
        public boolean isInteger();

        // @return the single integer that this NestedInteger holds, if it holds a single integer
        // Return null if this NestedInteger holds a nested list
        public Integer getInteger();

        // Set this NestedInteger to hold a single integer.
        public void setInteger(int value);

        // Set this NestedInteger to hold a nested list and adds a nested integer to it.
        public void add(NestedInteger ni);

        // @return the nested list that this NestedInteger holds, if it holds a nested list
        // Return null if this NestedInteger holds a single integer
        public List<NestedInteger> getList();
    }

    public class NestedInteger implements INestedInteger {
        public NestedInteger() {

        }

        public NestedInteger(int value) {

        }

        @Override
        public boolean isInteger() {
            return false;
        }

        @Override
        public Integer getInteger() {
            return null;
        }

        @Override
        public void setInteger(int value) {

        }

        @Override
        public void add(NestedInteger ni) {

        }

        @Override
        public List<NestedInteger> getList() {
            return null;
        }
    }

    public class Solution {
        public NestedInteger deserialize(String s) {
            if (s == null || s.isEmpty()) {
                return null;
            }
            if (s.charAt(0) != '[') {
                return new NestedInteger(Integer.valueOf(s));
            }
            Stack<NestedInteger> stack = new Stack<>();
            int start = 0;
            NestedInteger curr = null;
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                if (c == '[') {
                    if (curr != null) {
                        stack.push(curr);
                    }
                    curr = new NestedInteger();
                    start = i + 1;
                } else if (c == ']') {
                    String num = s.substring(start, i);
                    if (!num.isEmpty()) {
                        curr.add(new NestedInteger(Integer.valueOf(num)));
                    }
                    if (!stack.isEmpty()) {
                        NestedInteger top = stack.pop();
                        top.add(curr);
                        curr = top;
                    }
                    start = i + 1;
                } else if (c == ',') {
                    if (s.charAt(i - 1) != ']') {
                        String num = s.substring(start, i);
                        curr.add(new NestedInteger(Integer.valueOf(num)));
                    }
                    start = i + 1;
                }
            }
            return curr;
        }
    }
}
