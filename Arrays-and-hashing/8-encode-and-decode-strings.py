class Solution:
    def encode(self, s):
        encoded_string = ""
        for st in s:
            encoded_string += str(len(st)) + "#" +st
        return encoded_string

    def decode(self, s):
        decoded_string = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_string.append(s[j+1:j+1+length])
            i = j+1+length
        return decoded_string


# solution: we use a delimiter to encode the string and then use the delimiter to decode the string and use a hashmap to store the encoded string and the decoded string
# time complexity: O(n) - we iterate through the string once
# space complexity: O(n) - we store the encoded string
# leetcode: https://leetcode.com/problems/encode-and-decode-strings/
# explanation: https://www.youtube.com/watch?v=B1k_xCEpqAY
