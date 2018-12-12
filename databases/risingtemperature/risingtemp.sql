/* Problem 197 Leetcode */
SELECT W2.Id
FROM Weather as W1, Weather as W2
WHERE DATEDIFF(W2.RecordDate, W1.RecordDate) = 1 AND W1.Temperature < W2.Temperature;
