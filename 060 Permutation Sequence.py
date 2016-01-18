'''
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        factorial = 1
        for i in range(1, n):
            factorial *= i

        result = []
        array = list(range(1, n + 1))
        for i in range(n - 1, 0, -1):
            index = k // factorial
            result.append(str(array[index]))
            array = array[:index] + array[index + 1:]
            k %= factorial
            factorial //= i
        result.append(str(array[0]))
        return "".join(result)


if __name__ == "__main__":
    assert Solution().getPermutation(3, 3) == "213"
    assert Solution().getPermutation(9, 324) == "123685974"