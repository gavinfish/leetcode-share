import java.util.HashMap;
import java.util.Map;

/**
 * Created by drfish on 25/06/2017.
 */
public class _013RomanToInteger {
    public int romanToInt(String s) {
        Map<Character, Integer> map = new HashMap<Character, Integer>() {{
            put('M', 1000);
            put('D', 500);
            put('C', 100);
            put('L', 50);
            put('X', 10);
            put('V', 5);
            put('I', 1);
        }};
        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i > 0 && map.get(s.charAt(i)) > map.get(s.charAt(i - 1))) {
                result -= map.get(s.charAt(i - 1));
                result += map.get(s.charAt(i)) - map.get(s.charAt(i - 1));
            } else {
                result += map.get(s.charAt(i));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        _013RomanToInteger solution = new _013RomanToInteger();
        assert 12 == solution.romanToInt("XII");
        assert 21 == solution.romanToInt("XXI");
        assert 99 == solution.romanToInt("XCIX");
    }
}
