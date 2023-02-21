'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45'''

class CacheRecursiveSolution:
    def climbStairs(self, n: int) -> int:
        memo = [0 for n in range(n+1)]
        def climb(start, n):
            if start > n:
                return 0
            elif start == n:
                return 1
            elif memo[start]!=0:
                return memo[start]
            else:
                memo[start] = climb(start+1, n) + climb(start+2,n)
                return memo[start]
        return climb(0, n)

class BruteForceRecursiveSolution:
    def climbStairs(self, n: int) -> int:
        def climb(start, n):
            if start > n:
                return 0
            elif start == n:
                return 1
            else:
                return climb(start+1, n) + climb(start+2,n)
        return climb(1, n) + climb(2, n)
