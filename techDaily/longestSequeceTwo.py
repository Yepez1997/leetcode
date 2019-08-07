
''' 
findSequence: Given a sequence of numbers, find the longest sequence that contains two numbers 
'''
def findSequence(seq):
    unique = set()
    currentSequence = []
    for num in seq: 
        if num not in unique and len(unique) < 2:
            unique.add(num)
        elif num in unique:
            currentSequence.append(num)
    return len(currentSequence)

print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]) == 4)





