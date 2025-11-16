class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s) -1 
        while  start<end:
            while start< end  and not self.alphanum(s[start]):
                start+=1
            while end > start and not self.alphanum(s[end]):
                end -=1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                else :
                    start +=1
                    end -=1
        return True                        

        
    def alphanum(self, c ):
        return (
            (ord("A") <= ord(c) <= ord("Z"))
            or (ord("a") <= ord(c) <= ord("z"))
            or (ord("0") <= ord(c) <= ord("9"))
        )


# solution approach
# time complexity :- O(n)
# space complexity :- O(1)