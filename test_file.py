def problem_3(nums):
    seq = []
    seq_sum = 0

    s_p = 0
    max_l = []
    _sum = 0
    index = 0
    while index < len(nums):

        _sum = _sum + nums[index]

        if _sum < 0:
            s_p = index + 1
            max_l.append(_sum)
            _sum = 0

        else:
            max_l.append(_sum)

        index = index + 1

    seq_sum = max(max_l)
    e_p = max_l.index(seq_sum)
    seq = nums[s_p:e_p + 1]

    return seq, seq_sum


if __name__ == '__main__':
    nums = [1, 2, 3, 3, 4, 5, -4588345, 66, 7, 8]
    print(problem_3(nums))
