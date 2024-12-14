
def count_even_ones_by_pattern(num):
    # Convert num to binary and remove '0b' prefix
    bin_num = bin(num)[2:]
    
    # Zero number of 1s is even so 0 is evil
    count_e = 1
    
    # Calculate the sum of 2^n for n < len(bin_num) - 1
    count_e += sum(2**n for n in range(len(bin_num) - 2))
    
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
    count_e += odd_even_format[:num - 2**(len(bin_num)-1) + 1].count('e')
    
    return count_e

def count_even_ones_by_brute_force(num):
    res = 0
    for i in range(0, num+1):
        inter_sum = 0
        for char in bin(i)[2:]:
            if char == '1':
                inter_sum += 1
        if inter_sum % 2 == 0:
            res += 1
            # print(i, end = " ")
    # print()
    return res

num = 100
print(f"Evil numbers <= {num}:")
print("Count by brute force:", count_even_ones_by_brute_force(num))
print("Count by Thue-Morse sequence:", count_even_ones_by_pattern(num))
print()
num = 2025
print(f"Evil numbers <= {num}:")
print("Count by brute force:", count_even_ones_by_brute_force(num))
print("Count by Thue-Morse sequence:", count_even_ones_by_pattern(num))
