'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
'''

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        start = end = 0
        result, curr_words_length = [], 0
        for i, word in enumerate(words):
            if len(word) + curr_words_length + end - start  > maxWidth:
                if end - start == 1:
                    result.append(words[start] + ' ' * (maxWidth - curr_words_length))
                else:
                    total_space = maxWidth - curr_words_length
                    space, extra = divmod(total_space, end - start - 1)
                    for j in range(extra):
                        words[start + j] += ' '
                    result.append((' ' * space).join(words[start:end]))
                curr_words_length = 0
                start = end = i
            end += 1
            curr_words_length += len(word)
        result.append(' '.join(words[start:end]) + ' ' * (maxWidth - curr_words_length - (end - start - 1)))
        return result


if __name__ == "__main__":
    assert Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]