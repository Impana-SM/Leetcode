class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the result
        isPositive = (dividend < 0) == (divisor < 0)
        
        # Convert both numbers to positive
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        
        # Subtract divisor multiples from dividend
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # Double temp and multiple until temp << 1 exceeds dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            # Subtract the largest possible chunk
            dividend -= temp
            quotient += multiple
        
        # Apply sign
        if not isPositive:
            quotient = -quotient
        
        # Clamp to 32-bit integer range
        return max(min(quotient, 2**31 - 1), -2**31)
