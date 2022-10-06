def is_valid(isbn):
    nums = list(isbn.replace("-", ""))
    if len(nums) != 10:
        return False
    if nums[-1] == "X":
        nums[-1] = "10"
    if not all([c.isdigit() for c in nums]):
        return False
    return sum(int(x)*y for x, y in zip(nums, range(10, 0, -1))) % 11 == 0
