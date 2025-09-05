# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Leetcode problem: 739

def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0]*n
    stk = []

    for i,t in enumerate(temperatures):
        while stk and stk[-1][0]<t:
            stk_t,stk_i = stk.pop()
            answer[stk_i] = i - stk_i
        
        stk.append((t,i))

    return answer

temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))
