
def count_even_ones_by_pattern(num):
    # Convert num to binary and remove '0b' prefix
    bin_num = bin(num)[2:]
    
    # Calculate the sum of 2^n for n < len(bin_num) - 1
    count_e = sum(2**n for n in range(len(bin_num) - 2))
    
    # Initialize Odd_even_format
    odd_even_format = 'o'
    
    # Generate the odd-even format for len(bin_num) digits
    for _ in range(len(bin_num)-1):
        temp = odd_even_format
        for char in odd_even_format:
            if char == 'o':
                temp += 'e'
            elif char == 'e':
                temp += 'o'
        odd_even_format = temp
    
    # Count the number of 'e's in the first num - 2^(len(bin_num)) + 1 positions
    count_e += odd_even_format[:num - 2**(len(bin_num)) + 1].count('e')
    
    return count_e

def count_even_ones_by_brute_force(num):
    res = 0
    for i in range(2, num+1):
        inter_sum = 0
        for char in bin(i)[2:]:
            if char == '1':
                inter_sum += 1
        if inter_sum % 2 == 0:
            res += 1
    return res

num = 10
print("Count by pattern:", count_even_ones_by_pattern(num))
print("Count by brute force:", count_even_ones_by_brute_force(num))
