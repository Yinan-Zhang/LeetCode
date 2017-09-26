def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip();
        words = s.split(" ")
        reverse = []
        for word in words:
            if len(word) > 0:
                reverse = [word] + reverse

        reverse_s = ""
        for word in reverse:
            reverse_s += word + " "
        reverse_s = reverse_s[:-1]
        return reverse_s
