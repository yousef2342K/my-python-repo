
def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Args:
        nums: A list of integers.
        target: An integer.

    Returns:
        A list of two integers, the indices of the two numbers such that they add up to target.
     """



    seen_list = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen_list:
            return [seen[complement], i]
        seen[num] = i
    raise ValueError("No two sum solution")
