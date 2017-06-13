import java.util.Arrays;
import java.util.Stack;

/**
 * Given an absolute path for a file (Unix-style), simplify it.
 * <p>
 * For example,
 * path = "/home/", => "/home"
 * path = "/a/./b/../../c/", => "/c"
 * click to show corner cases.
 * <p>
 * Corner Cases:
 * Did you consider the case where path = "/../"?
 * In this case, you should return "/".
 * Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
 * In this case, you should ignore redundant slashes and return "/home/foo".
 * <p>
 * Created by drfish on 6/7/2017.
 */
public class _071SimplifyPath {
    public String simplifyPath(String path) {
        if (path == null) {
            return "";
        }
        String[] parts = path.split("/");
        Stack<String> stack = new Stack<>();
        for (String part : parts) {
            switch (part) {
                case ".":
                    break;
                case "":
                    break;
                case "..":
                    if (!stack.isEmpty()) {
                        stack.pop();
                    }
                    break;
                default:
                    stack.push(part);
            }
        }

        String result = "";
        for (String s : stack) {
            result += "/" + s;
        }
        return result.length() == 0 ? "/" : result;
    }

    public static void main(String[] args) {
        _071SimplifyPath solution = new _071SimplifyPath();
        assert "/home".equals(solution.simplifyPath("/home/"));
        assert "/c".equals(solution.simplifyPath("/a/./b/../../c/"));
        assert "/".equals(solution.simplifyPath("/home/../../.."));
    }
}
