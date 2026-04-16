class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        
        def backtrack(start, path):
            # If we got 4 parts
            if len(path) == 4:
                if start == len(s):
                    result.append(".".join(path))
                return
            
            # Try 1 to 3 digits
            for i in range(1, 4):
                if start + i > len(s):
                    break
                
                part = s[start:start+i]
                
                # Check validity
                if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                    continue
                
                backtrack(start + i, path + [part])
        
        backtrack(0, [])
        return result