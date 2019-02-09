# given an array find if there exists two numbers 
# that add up to k and return indicies x1 and x2 



def twosum(arr, target):
    nums_dict = {}
    for i in range(0, len(arr)):
        nums_dict[arr[i]] = i
    for i in range(0, len(arr)):
        num2 = target - arr[i]
        if (num2 in nums_dict) and (nums_dict.get(num2) != i):
            return [i, nums_dict.get(num2)]

def tests():
    if (twosum([1,2,3,2],5) == (2,3) or (3,2)):
        print("Passed Case 1")
    return 0

tests()

