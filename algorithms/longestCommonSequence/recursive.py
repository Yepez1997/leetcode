# Given a sequence, find the longest common subsequence
# @author Aureliano Yepez 


# let i and j be the indices of the words, 
# if i == j ->  recurse on i-j 
# if not we want to find max(i,j-1 and i-1,j)
def lcs(X,Y,x_len,y_len):
    if x_len == 0 or y_len == 0:
        return 0
    elif X[x_len - 1] == Y[y_len - 1]:
        return 1 + lcs(X, Y, x_len - 1, y_len - 1)
    else:
        return max(lcs(X, Y, x_len - 1, y_len), lcs(X, Y, x_len, y_len - 1))


# must assert all are true to pass
X = "AGGTAB"
Y = "GXTXAYB"
x_len = len(X)
y_len = len(Y)


def tests():
    X = "AGGTAB"
    Y = "GXTXAYB"
    x_len = len(X)
    y_len = len(Y)

    assert(lcs(X,Y,x_len,y_len) == 4)
    print("Passed 1")

tests()

