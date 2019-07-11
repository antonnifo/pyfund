list = [3,5,8,11,1,-1,6]

def check_sum(nums, target=10):
    '''check in a given a list if two integers add up to a
       given target which default value is 10.
       
       Args:
            nums:list of integers.
            target:the sum.
       Returns:
            two intergers that add up to target or None is no
            intergers that add up to target. 
    '''
    index_map = {}
    for index in range(len(nums)):
        num = nums[index]
        pair = target - num

        if pair in index_map:
            return [pair, nums[index]]
        index_map[num] = index
    return None

if __name__ == "__main__":
    print(check_sum(list))
