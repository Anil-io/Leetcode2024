class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        split = list(s)
        
        # Convert words to number 
        numbers = [(ord(split[i]) - ord("a") +1) for i in range(len(split))]

        #convert the numbers to individual digits and Add the digits K times 
        for iter in range(k):
            numbers =  [sum([int(digit) for num in numbers for digit in str(num)])]

        return numbers[0]
    
a = Solution()
b = a.getLucky(s="anil",k=1)

