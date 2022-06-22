def mult(*nums):
    mult_num = 1

    for num in nums:
        mult_num *= num
    
    return mult_num

print(mult(2, 2, 5))