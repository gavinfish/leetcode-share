/**
 * Reverse digits of an integer.
 * <p>
 * Example1: x = 123, return 321
 * Example2: x = -123, return -321
 * <p>
 * Have you thought about this?
 * Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
 * <p>
 * If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
 * Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of
 * 1000000003 overflows. How should you handle such cases?
 * For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
 * <p>
 * Note:
 * The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer
 * overflows.
 * <p>
 * Created by drfish on 25/06/2017.
 */
public class _007ReverseInteger {
    public int reverse(int x) {
        int result = 0;
        while (x != 0) {
            int tail = x % 10;
            int temp = result * 10 + tail;
            if ((temp - tail) / 10 != result) {
                return 0;
            }
            result = temp;
            x /= 10;
        }
        return result;
    }

    public static void main(String[] args) {
        _007ReverseInteger solution = new _007ReverseInteger();
        assert 321 == solution.reverse(123);
        assert -321 == solution.reverse(-123);
        assert 0 == solution.reverse(2147483647);
    }
}
