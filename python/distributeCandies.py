class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        distribution = [0] * num_people
        i = 1
        while candies > 0:
            # add the minimum between the number of candies left and the current amount you have
            distribution[(i-1)%num_people] += min(i, candies)
            # map into the right person and add the total candies left to add to that person
            candies = candies - i
            i += 1
        return distribution

