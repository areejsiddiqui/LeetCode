class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]   #reversing array
        one, i =   1, 0            #2 variables one and i, one is keeping track of the carry and initialized to 1 cause we have to add at least a single 1,
                                # and i for the index of the gigit we are currently at and initialezed to beginniing of array i.e 0
        while one:                            #were gonna continue to iterate thru digits while one ==1
            if i<len(digits):         #if i is in bounds, we ofc increment, when eg array 9,9,9 is incremented it becomes 1000, out of bounds, thats handled by else
                if digits[i] == 9:   #then we have carry
                    digits[i] = 0     #one = 1,one is gonna stay the value 1 , first digit is reset to 0, cuse we reversed, basically 19 + 1= 20, 91=02
                else:                 #if digit is not 9,
                    digits[i] += 1
                    one = 0            #we ordinarily increment, no carry , so one = 0
            else:                       #when we go out of bounds, we reached the end, no more digits to add to anymore, but e still have a carry on 
                digits.append(1)        #adding a new digit to the array
                one = 0                 #we dont have a carry anymore so reset one to 0, terminates while loop
            i += 1                      #dont forget incrementing index whith while loop
        return digits[::-1]             #reverse the array again



    #time complexity is O(n) cause we are traversing entire input array which is of length n
    #space complexity is O(1) cause we dont need any more memory other than the memory for input array