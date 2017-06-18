/**
 * Write a program to find the nth super ugly number.
 * <p>
 * Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For
 * example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given
 * primes = [2, 7, 13, 19] of size 4.
 * <p>
 * Note:
 * (1) 1 is a super ugly number for any given primes.
 * (2) The given numbers in primes are in ascending order.
 * (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
 * (4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
 * <p>
 * Credits:
 * Special thanks to @dietpepsi for adding this problem and creating all test cases.
 * <p>
 * Created by drfish on 16/06/2017.
 */
public class _313SuperUglyNumber {
    public int nthSuperUglyNumber(int n, int[] primes) {
        int[] indexes = new int[primes.length];
        int[] superUgly = new int[n];

        superUgly[0] = 1;
        for (int i = 1; i < n; i++) {
            superUgly[i] = Integer.MAX_VALUE;
            for (int j = 0; j < primes.length; j++) {
                superUgly[i] = Math.min(superUgly[i], primes[j] * superUgly[indexes[j]]);
            }
            for (int j = 0; j < primes.length; j++) {
                while (primes[j] * superUgly[indexes[j]] <= superUgly[i]) {
                    indexes[j]++;
                }
            }
        }
        return superUgly[n - 1];
    }

    public static void main(String[] args) {
        _313SuperUglyNumber solution = new _313SuperUglyNumber();
        assert 32 == solution.nthSuperUglyNumber(12, new int[]{2, 7, 13, 19});
    }
}
