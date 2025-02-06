def lengthOfLongestSubstring(s: str) -> int:
        # use a map to store the substring's elements to index, one to one
        position = {}
        length = 1
        l, r = 0, 0
        position[s[r]] = r
        while l <= r and r < len(s)-1:
            print("left={}, right = {}".format(s[l], s[r]))
            r += 1
            # left, right = s[l], s[r]
            if s[r] not in position:
                position[s[r]] = r
                length = max(length, r-l+1)
                continue
            
            # if duplicate found, move to the next element
            old_r_position = position[s[r]]
            while l <= old_r_position:
                position.pop(s[l])
                l += 1
            position[s[r]] = r # update new position
            
        return length


print(lengthOfLongestSubstring("abc"))
