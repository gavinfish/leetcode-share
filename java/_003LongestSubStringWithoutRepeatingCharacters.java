import java.util.HashMap;
import java.util.Map;

/**
 * Given a string, find the length of the longest substring without repeating characters.
 * <p>
 * Examples:
 * Given "abcabcbb", the answer is "abc", which the length is 3.
 * Given "bbbbb", the answer is "b", with the length of 1.
 * Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
 * subsequence and not a substring.
 * Created by drfish on 13/05/2017.
 */
public class _003LongestSubStringWithoutRepeatingCharacters {
    public int lengthOfLongestSubstring(String s) {
        if (s == null)
            return 0;
        if (s.length() <= 1)
            return s.length();
        Map<Character, Integer> map = new HashMap<>();
        int start = -1;
        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i))) {
                start = Math.max(start, map.get(s.charAt(i)));
            }
            map.put(s.charAt(i), i);
            result = Math.max(result, i - start);
        }
        return result;
    }

    public static void main(String[] args) {
        _003LongestSubStringWithoutRepeatingCharacters solution = new _003LongestSubStringWithoutRepeatingCharacters();
        assert 3 == solution.lengthOfLongestSubstring("abcabcbb");
        assert 1 == solution.lengthOfLongestSubstring("bbbbb");
        assert 3 == solution.lengthOfLongestSubstring("pwwkew");
    }
}
