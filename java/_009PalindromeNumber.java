/**
 * Determine whether an integer is a palindrome. Do this without extra space.
 * <p>
 * Some hints:
 * Could negative integers be palindromes? (ie, -1)
 * <p>
 * If you are thinking of converting the integer to string, note the restriction of using extra space.
 * <p>
 * You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that
 * the reversed integer might overflow. How would you handle such case?
 * <p>
 * There is a more generic way of solving this problem.
 * <p>
 * Created by drfish on 25/06/2017.
 */
public class _009PalindromeNumber {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x != 0 && x % 10 == 0)) {
            return false;
        }
        int reverse = 0;
        while (x > reverse) {
            reverse = reverse * 10 + x % 10;
            x /= 10;
        }
        return (x == reverse || x == reverse / 10);
    }

    public static void main(String[] args) {
        _009PalindromeNumber solution = new _009PalindromeNumber();
        assert solution.isPalindrome(12321);
        assert solution.isPalindrome(123321);
        assert !solution.isPalindrome(-121);
    }
}
