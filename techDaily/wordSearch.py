''' wordSearch - You are given a 2D array of characters, and a target string. Return whether 
or not the word target word exists in the matrix. Unlike a standard word search,
 the word must be either going left-to-right, or top-to-bottom in the matrix. '''

 # word_search - check if a word exists by going strictly right or down
def word_search(matrix, word):
    for row in range(len(matrix)):
        rowLen = len(matrix)
        for col in range(len(matrix[row])):
            coLen = len(matrix[row])
            search_right = searchRight(row, col, coLen, matrix)
            search_down = searchDown(row, col, rowLen, matrix)
            if word in (search_right, search_down):
                return True
    return False 


# searchRight - traverse soley up to the end of the col
def searchRight(row, col, length, matrix):
    word  = ""
    for i in range(length):
        word += matrix[row][i]
    return word 


# searchDown - traverse soley up to the end of the row 
def searchDown(row, col, length, matrix):
    word = ""
    for j in range(length):
        word += matrix[j][col]
    return word
  
matrix = [
  ['F', 'A', 'C', 'I'],
  ['O', 'B', 'Q', 'P'],
  ['A', 'N', 'O', 'B'],
  ['M', 'A', 'S', 'S']]

print(word_search(matrix, 'FOAM') == True)
