def solution(phone_book):
    d = {}
    for nums in phone_book:
        d[nums] = 1
    for nums in phone_book:
        prefix = ""
        for num in nums:
            prefix += num
            
            if prefix in d and prefix != nums:
                return False
    return True