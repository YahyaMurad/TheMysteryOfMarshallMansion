class StringMatching:
    def __init__(self):
        pass
    
    def brute_force(self, text, pattern):
        n = len(text)
        m = len(pattern)
        
        if n != m:
            return False

        for i in range(n):
            if text[i] != pattern[i]:
                return False
            
        return True
    
    def pi(self, pattern):
        n = len(pattern)

        pi = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and pattern[j] != pattern[i]:
                j = pi[j-1]
            if pattern[j] == pattern[i]:
                j += 1
            pi[i] = j

        return pi


    def kmp(self, string, pattern):
        n = len(string)
        m = len(pattern)

        PI = self.pi(pattern)

        j = 0
        matches = []
        for i in range(n):
            while j > 0 and pattern[j] != string[i]:
                j = PI[j-1]
            if pattern[j] == string[i]:
                j += 1
            if j == m:
                matches.append(i-m+1)
                j = PI[j-1]

        return True if len(matches) > 0 else False 