def maior(*nums):
    maior_num = nums[0]

    for num in nums:
        if num > maior_num:
            maior_num = num
    
    return maior_num

print(maior(2, 1, 6, 0, 10, 15, 9))