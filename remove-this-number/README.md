# Challenge #2

## Hint:

### find all multiples of 3 and 5 in the number 666, sum them.

#### Flag: 103298


    def find_sum(maximum):
        _sum = 0
        for i in range(maximum):
            if (i % 3 == 0) or (i % 5 == 0): _sum = _sum + i
        return _sum

    if __name__ == '__main__':
        maximum = 666
        flag = find_sum(maximum)
        print(flag)

# Challenge #3 >> advanced

## Hint: 

### Use the flag from challenge #2, remove ALL occurences of challenge #2's flag from nums.txt, then sum the remaining numbers.

#### Flag: 49991650686095845532282651

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

        from solution2 import find_sum

        maximum = 666
        flag = find_sum(maximum)
        nums = find_and_remove('./nums.txt', 'newfile.txt', str(flag))
    
        print(get_sum(nums)
