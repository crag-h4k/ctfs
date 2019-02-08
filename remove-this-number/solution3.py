#Challenge #3 >> advanced
#Use the flag from challenge #2, remove ALL occurences of challenge #2's flag from nums.txt, then sum the remaining numbers.

def find_and_remove(fname, new_file, flag):
    with open(fname, 'r') as f:
        nums = f.readlines()
    _nums = nums
    print(flag)
    j = 0 
    for i in nums:
        if flag in i: del _nums[j]
        j = j + 1

    with open(new_file, 'w') as f:
        f.writelines(_nums)
    return _nums

def get_sum(nums):
    _sum = 0
    for i in nums:
        _sum = _sum + int(i)
    print(_sum)
    return _sum

if __name__ == '__main__':

    from challenge import find_sum

    maximum = 666
    flag = find_sum(maximum)
    nums = find_and_remove('./nums.txt', 'newfile.txt', str(flag))
    
    get_sum(nums)
