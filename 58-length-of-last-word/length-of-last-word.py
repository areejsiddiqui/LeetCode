class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i, length = len(s)-1, 0         #initialize pointers i to last index of string, and length to first index of string

        while s[i] == " ":
            i-=1                                 #decrement i as long as we see spaces
          
        while  i >= 0 and s[i] != " ":                                 
            length += 1                         
            i-=1
        return length                                         
                
                
                
                
         
        #--------while  i >= 0 and s[i] != " ":-----------  # i should  not out of bounds i.e it cannot , counting no. of consecutvive chars before reach #end of string, or we reach a space, if we get to any of these, we exit the loop
                
                
                
                
                # MY UNDERSTANDING ----- If last character i.e. len(s)-1 = " " space, then keep iterating i pointer till it encounters a character , once it encounters a character which it will, start counting the number of letters that u encounter till " " space is encountered, thast how we et the last word, irrespecitve of there being space after the last word or not. and how to count number of characters in the string, u note the position where i first encounters a character when it starts iterating from the end of the string, u note the index is say 10 as in the case of d in hello world, and then idk if u use a stack or a queue, but my understanding is, u note this particular position, iterate i i.e i++, and then when a space is encountered, say at index 5 in "hello world", you subtract 10-5, u return length of the last word = s[j]-s[k], assuming if we're using 2 different pointers here, one that stays at the first character it encounters when it start iterating