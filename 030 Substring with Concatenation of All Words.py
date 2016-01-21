'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        s_length = len(s)
        word_num = len(words)
        word_length = len(words[0])
        words_length = word_num * word_length
        result = []
        words_dict = {}
        for word in words:
            words_dict[word] = words_dict[word] + 1 if word in words_dict else 1
        for i in range(word_length):
            left = i
            right = i
            curr_dict = {}
            while right + word_length <= s_length:
                word = s[right:right + word_length]
                right += word_length
                if word in words_dict:
                    curr_dict[word] = curr_dict[word] + 1 if word in curr_dict else 1
                    while curr_dict[word] > words_dict[word]:
                        curr_dict[s[left:left + word_length]] -= 1
                        left += word_length
                    if right - left == words_length:
                        result.append(left)
                else:
                    curr_dict.clear()
                    left = right
        return result


if __name__ == "__main__":
    assert Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9]