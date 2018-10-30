class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # if the input doesn't any text
        if '.' not in input:
            return 0
        if '\n' not in input:
            return len(input)

    def recursion(self, input, level, length):
         #"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
        if '\t' not in input:
            return input+length
        else:
            next_level = input.split('\t'*level)[1:]
            return max([self.recursion(next_level, level+1, 

