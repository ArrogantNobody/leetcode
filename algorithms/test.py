list = [1,2,3,1,2,3]

def containsNearbyDuplicate(nums, k):
    tmp = dict()
    res = 0
    for index, item in enumerate(nums):
        if item not in tmp.keys():
            tmp[item] = index
        else:
            res = max(res, abs(tmp[item] - index))

            tmp[item] = index
            print('in')
    print(res)
    print(tmp)
    return res <= k
containsNearbyDuplicate(list, 2)